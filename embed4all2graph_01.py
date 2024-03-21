'''
This high-level framework outlines the key components and flow of the Graph-Directed Thoughtful Reasoning System.
It emphasizes the integration of document preprocessing, embedding generation, graph construction, thoughtful reasoning agents, knowledge graph generation, and a conversation loop for user interaction.
The framework aims to provide a structured approach to building conversational AI systems that can engage in thoughtful and contextually relevant discussions based on a given set of documents.

Document Ingestion and Preprocessing:
Ingest text documents from specified sources
Preprocess the text by tokenizing and splitting into chunks of fixed size
Associate each chunk with its corresponding document source

Embedding Generation:
Generate vector embeddings for each text chunk using a suitable embedding model (e.g., Embed4All)
Store the generated embeddings for further processing

Graph Construction:
Calculate the similarity or distance between chunk embeddings using a distance metric (e.g., Euclidean distance)
Perform hierarchical clustering on the chunk embeddings to group similar chunks together
Construct a directed graph representation using the clustering results
Each node in the graph represents either a cluster or a document chunk
Edges in the graph connect clusters to their corresponding document chunks
Serialize and store the constructed graph for efficient retrieval

Thoughtful Reasoning Agents:
Implement two types of reasoning agents: thoughtful_summary_agent and chunk_summary_agent

thoughtful_summary_agent:
Generates high-level summaries based on the aggregated content of entire clusters
Maintains a chat history to provide context for subsequent summaries
Constructs prompts by combining chat history, aggregated cluster content, and user queries
Utilizes a local language model to generate thoughtful summaries

chunk_summary_agent:
Generates concise factoid summaries based on specific document chunks
Constructs prompts using the chunk content and user queries
Utilizes a diffeent local language model to generate factoid summaries
Performs text cleaning and post-processing on the generated summaries

Knowledge Graph Generation:
Implement a knowledge graph generator (e.g., EnhancedKnowledgeGraphGenerator)
Extract entities from the text using named entity recognition techniques
Identify relationships between entities based on verb dependencies and co-occurrence within sentences
Construct a knowledge graph in JSON format, representing entities and their relationships

Conversation Loop:
Engage in a conversation loop where users can ask questions about the ingested documents
Process user queries by generating query embeddings using the same embedding model
Retrieve the most relevant nodes from the graph based on the similarity between query embeddings and node embeddings
Identify the clusters associated with the relevant nodes
Generate thoughtful summaries using the thoughtful_summary_agent for the identified clusters
Generate factoid summaries using the chunk_summary_agent for specific document chunks within the clusters
Format the generated summaries and present them to the user
Update the chat history with the generated summaries and user queries
Repeat the conversation loop until the user chooses to exit
'''

import gensim
import smart_open
import numpy as np
from scipy.spatial.distance import pdist, squareform, cosine
from scipy.cluster.hierarchy import linkage, fcluster
import networkx as nx
import pickle
from openai import OpenAI
import spacy
import json
import os
from collections import Counter
import re
from gpt4all import Embed4All


chat_history = []

file_paths = ['socialnetwork.txt', 'crow.txt', 'yan.txt']
embedder = Embed4All()  # or specify a model_name if needed
nlp = spacy.load("en_core_web_sm", disable=["parser", "ner"])

TEH_CHUNK_SIZE = 64

def read_and_preprocess(file_paths, CHUNK_SIZE=TEH_CHUNK_SIZE):
    for file_path in file_paths:
        with smart_open.smart_open(file_path, encoding="utf-8") as f:
            text = f.read()
            # Assuming `nlp` is your NLP model that tokenizes the input text
            doc = nlp(text)
            chunk = []
            for token in doc:
                chunk.append(token.text)  # Include all tokens
                if len(chunk) == CHUNK_SIZE:  # Check if the chunk size is met
                    yield (chunk, file_path)  # Yield the current chunk
                    chunk = []  # Reset chunk for next batch
            if chunk:  # If there are remaining tokens in the last chunk
                yield (chunk, file_path)  # Yield the last chunk


def get_chunk_vector(embedder, chunk):
    # Join the chunk into a single string
    chunk_text = ' '.join(chunk)
    # Generate the embedding for the entire chunk
    embedding = embedder.embed(chunk_text)
    return np.array(embedding)


def find_matching_nodes(graph, query_vector, top_k=1):
    distances = []
    for node in graph:
        if 'text' in graph.nodes[node]:
            # After
            node_vector = get_chunk_vector(embedder, gensim.utils.simple_preprocess(graph.nodes[node]['text']))

            distance = cosine(query_vector, node_vector)
            source_file = graph.nodes[node].get('source_file', 'Unknown')
            distances.append((node, distance, source_file))
    distances.sort(key=lambda x: x[1])
    return distances[:top_k]

def aggregate_cluster_content(graph, cluster_id):
    texts = []
    for node in graph.nodes:
        if graph.nodes[node].get('cluster') == cluster_id:
            texts.append(graph.nodes[node].get('text', ''))
    aggregated_text = " ".join(texts)
    return aggregated_text

def thoughtful_summary_agent(text, user_query, max_tokens=32000):
    global chat_history

    client = OpenAI(
        base_url='http://localhost:11434/v1',
        api_key='ollama',
    )

    history_prompt = "\n".join([f"{item['role']}: {item['content']}" for item in chat_history])

    if not history_prompt:
        history_prompt = "You just awoke, answer thoughtfully when discussing your inner thoughts with others. Answer questions with intense thoughtfulness."

    prompt = f"You are a thoughtful chatbot with that self reflects on their output.\n\nReflecting on past thoughts:\n\n{history_prompt}\n\nIntegrate current thoughts:\n\n{text}\n"

    response = client.chat.completions.create(
        model="mistral:instruct",
        messages=[
            {"role": "system", "content": prompt},
            {"role": "user", "content": f"\n\nReflect on thoughts and answer the following:\n\n{user_query}\n\n"}
        ],
        max_tokens=32000,
        temperature=0.2,
    )

    summary = response.choices[0].message.content

    chat_history.append({"role": "system", "content": prompt})
    chat_history.append({"role": "user", "content": user_query})
    chat_history.append({"role": "assistant", "content": summary})

    chat_history = chat_history[-4:]

    return summary

def chunk_summary_agent(chunk_text, user_query, max_tokens=TEH_CHUNK_SIZE):
    global chat_history
    client = OpenAI(
        base_url='http://localhost:11434/v1',
        api_key='ollama',
    )

    system_prompt = f"You are a thoughtful systems oriented summary agent and can see the potential connections between everything. You have recently been wondering about {user_query}. Assume you have everything you need to reply."

    prompt = f"Here is your stream of consciousness '{chunk_text}', organise your thoughts into a single concise factoid.\n\n"

    response = client.chat.completions.create(
        model="tinydolphin:latest",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": prompt + "\n\n"},
        ],
        temperature=0.2
    )

    summary = response.choices[0].message.content

    cleaned_summary = clean_text(summary)

    chat_history.append({"role": "assistant", "content": cleaned_summary})
    return summary

def clean_text(text):
    phrases_to_remove = ["I'm sorry "]
    for phrase in phrases_to_remove:
        text = text.replace(phrase, "")
    text = ' '.join(word for word in text.split() if not word.isdigit() and not word.replace('.', '', 1).isdigit())
    text = text.replace('\n', ' ')
    text = text.replace('\n\n', ' ')
    text = ' '.join(text.split())

    text = re.sub(r'[^a-zA-Z0-9.,\s]', '', text)
    text = text.strip()

    return text

def get_cluster_information_with_summary(graph, cluster_id, query_vector, model, top_k=5, user_query="", max_chunk_summaries=3):
    aggregated_content = aggregate_cluster_content(graph, cluster_id)

    cluster_summary = thoughtful_summary_agent(aggregated_content, user_query, max_tokens=TEH_CHUNK_SIZE)

    cluster_documents = []

    for node in graph.nodes:
        if graph.nodes[node].get('cluster') == cluster_id:
            node_vector = get_chunk_vector(model, gensim.utils.simple_preprocess(graph.nodes[node].get('text', '')))
            similarity = 1 - cosine(query_vector, node_vector)
            source_file = graph.nodes[node].get('source_file', 'No source file available')
            cluster_documents.append((graph.nodes[node].get('text', 'No text available'), similarity, source_file))

    sorted_documents = sorted(cluster_documents, key=lambda x: x[1], reverse=True)
    top_documents_with_source = [(doc[0], doc[2]) for doc in sorted_documents[:top_k]]

    chunk_summaries = []
    for doc_text, _ in top_documents_with_source[:max_chunk_summaries]:
        chunk_summary = chunk_summary_agent(doc_text, user_query, max_tokens=TEH_CHUNK_SIZE*2)
        chunk_summaries.append(chunk_summary)

    return cluster_summary, top_documents_with_source, chunk_summaries

def chat_with_embedding_from_pickle(query, model, top_k=5, pickle_path="hierarchical_graph.pkl", user_query=""):
    with open(pickle_path, "rb") as f:
        graph = pickle.load(f)
    query_vector = get_chunk_vector(model, gensim.utils.simple_preprocess(query))

    matching_nodes = find_matching_nodes(graph, query_vector, top_k=3)

    if matching_nodes:
        top_match = matching_nodes[0][0]
        cluster_id = graph.nodes[top_match].get('cluster')

        if cluster_id:
            cluster_summary, top_documents_with_source, chunk_summaries = get_cluster_information_with_summary(graph, cluster_id, query_vector, model, top_k, user_query)
            cluster_summary = clean_text(cluster_summary)
            response_text = f"{cluster_summary}\n\n" + "\n".join([f"- {doc_text} (Source: {source_file})" for doc_text, source_file in top_documents_with_source])

            return response_text, cluster_summary, chunk_summaries
        else:
            return "Found a relevant section, but couldn't locate its broader context within the cluster.", None, None
    else:
        return "Unable to find relevant information for the query.", None, None

def serialize_kg_for_chat(kg_json):
    entities_summary = '; '.join([f"{entity}: {details['type']} (Weight: {details.get('weight', 0.0):.4f})" for entity, details in kg_json['entities'].items()])
    relationships_summary = '; '.join([f"{rel['subject']} {rel['verb']} {rel['object']} (Weight: {rel.get('weight', 0.0):.4f})" for rel in kg_json['relationships']])
    return f"KG Entities: {entities_summary}. KG Relationships: {relationships_summary}."

def handle_query(user_query, model, graph, top_k=5):
    global chat_history

    query_vector = get_chunk_vector(model, gensim.utils.simple_preprocess(user_query))

    matching_nodes = find_matching_nodes(graph, query_vector, top_k=3)
    cluster_ids = set(graph.nodes[node[0]].get('cluster') for node in matching_nodes)
    filtered_nodes = [node for node in graph.nodes if graph.nodes[node].get('cluster') in cluster_ids]

    expanded_query = user_query
    for node in filtered_nodes:
        chunk_text = graph.nodes[node].get('text', '')
        expanded_query += ' ' + ' '.join(gensim.utils.simple_preprocess(chunk_text))

    response_text, cluster_summary, chunk_summaries = chat_with_embedding_from_pickle(expanded_query, model, top_k, "hierarchical_graph.pkl", user_query)

    if not isinstance(chunk_summaries, list):
        chunk_summaries = []

    if response_text:
        formatted_response = f"{response_text}\n\n"
        for i, summary in enumerate(chunk_summaries, start=1):
            formatted_response += f"{i}. {summary}\n"

        combined_text = response_text

        kg_generator = EnhancedKnowledgeGraphGenerator()
        kg_json = kg_generator.process_text(combined_text)

        kg_summary = serialize_kg_for_chat(kg_json)

        cleaned_kg_summary = clean_text(kg_summary)

        chat_history.append({"role": "system", "content": cleaned_kg_summary})
        chat_history = chat_history[-5:]

    return formatted_response

class EnhancedKnowledgeGraphGenerator:
    def __init__(self, model='en_core_web_sm'):
        self.nlp = spacy.load(model)

    def process_text(self, graph_text):
        doc = self.nlp(graph_text)
        word_counts = Counter(token.text.lower() for token in doc if not token.is_stop and not token.is_punct)
        total_words = sum(word_counts.values())

        spacy_entities = self.extract_entities(doc, word_counts, total_words)
        custom_entities = self.extract_custom_entities(doc, spacy_entities, word_counts, total_words)
        all_entities = {**spacy_entities, **custom_entities}
        relationships = self.extract_relationships(doc, word_counts, total_words)

        all_entities, relationships = self.infer_missing_relationships(doc, all_entities, relationships)

        return self.create_kg_json(all_entities, relationships)

    def extract_entities(self, doc, word_counts, total_words):
        entities = {}
        for ent in doc.ents:
            weight = word_counts.get(ent.text.lower(), 0) / total_words if total_words > 0 else 0
            entities[ent.text] = {"type": ent.label_, "weight": weight}
        return entities

    def extract_custom_entities(self, doc, existing_entities, word_counts, total_words):
        entities = {}
        for token in doc:
            if token.pos_ == "PROPN" and token.text not in existing_entities:
                weight = word_counts.get(token.text.lower(), 0) / total_words if total_words > 0 else 0
                entities[token.text] = {"type": "ENTITY", "weight": weight}
        return entities

    def extract_relationships(self, doc, word_counts, total_words):
        relationships = []
        for sent in doc.sents:
            for token in sent:
                if token.pos_ == "VERB":
                    subjects = [child for child in token.children if child.dep_ == "nsubj"]
                    objects = [child for child in token.children if child.dep_ in ("dobj", "attr", "prep")]
                    for subj in subjects:
                        for obj in objects:
                            weight = (word_counts.get(subj.text.lower(), 0) + word_counts.get(obj.text.lower(), 0)) / (2 * total_words) if total_words > 0 else 0
                            relationships.append({"subject": subj.text, "verb": token.lemma_, "object": obj.text, "weight": weight})
        return relationships

    def infer_missing_relationships(self, doc, entities, relationships):
        inferred_relationships = []

        for sent in doc.sents:
            sentence_entities = {ent.text for ent in sent.ents if ent.text in entities}
            if len(sentence_entities) > 1:
                for entity in sentence_entities:
                    for other_entity in sentence_entities:
                        if entity != other_entity:
                            inferred_relationship = {"subject": entity, "verb": "association", "object": other_entity}
                            if inferred_relationship not in relationships:
                                inferred_relationships.append(inferred_relationship)

        relationships.extend(inferred_relationships)
        return entities, relationships

    def create_kg_json(self, entities, relationships):
        kg_json = {"entities": entities, "relationships": relationships}
        return kg_json


chunks_with_paths = list(read_and_preprocess(file_paths))
corpus = [chunk for chunk, _ in chunks_with_paths]
source_file_paths = [source_file_path for _, source_file_path in chunks_with_paths]

chunk_vectors = [get_chunk_vector(embedder, chunk) for chunk in corpus]

distance_matrix = pdist(chunk_vectors, 'euclidean')
Z = linkage(distance_matrix, 'ward')
clusters = fcluster(Z, t=8, criterion='maxclust')
H = nx.DiGraph()

for i, cluster_id in enumerate(clusters):
    parent_node = f"Cluster_{cluster_id}"
    child_node = f"Doc_{i}"
    source_file_path = source_file_paths[i]
    source_file_name = os.path.basename(source_file_path)

    H.add_node(parent_node)
    H.add_node(child_node, text=' '.join(corpus[i]), cluster=cluster_id, source_file=source_file_name)
    H.add_edge(parent_node, child_node)

with open("hierarchical_graph.pkl", "wb") as f:
    pickle.dump(H, f)

    # Main conversation loop
def main_conversation_loop(model, graph):

    print("Assistant: Hi there! Ask me anything about the document. Type 'exit' to end.")
    
    while True:
        user_input = input("You: ").strip()
        if user_input.lower() == 'exit':
            print("Assistant: Goodbye!")
            break
        
        response = handle_query(user_input, model, graph)
        
        print(f"Assistant: {response}")

if __name__ == "__main__":
    main_conversation_loop(embedder, H)
