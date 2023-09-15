from itertools import cycle
from gpt4all import GPT4All, Embed4All
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

class TechniqueRotatingTemplateGPT4All:
    def __init__(self, model_path):
        self.model = GPT4All(model_path)
        self._techniques = {
    "breathing_techniques": [
      {
        "name": "Diaphragmatic Breathing",
        "steps": [
          "Sit comfortably, with your knees bent and your shoulders, head, and neck relaxed.",
          "Place one hand on your upper chest and the other just below your rib cage.",
          "Breathe in slowly through your nose so that your stomach moves out against your hand.",
          "Exhale through pursed lips as you tighten your stomach muscles."
        ]
      },
      {
        "name": "4-7-8 Breathing",
        "steps": [
          "Close your mouth and inhale quietly through your nose to a count of 4.",
          "Hold your breath for a count of 7.",
          "Exhale completely through your mouth to a count of 8.",
          "Repeat the cycle three more times for a total of four breaths."
        ]
      },
      {
        "name": "Box Breathing",
        "steps": [
          "Sit upright and exhale all the air from your lungs.",
          "Inhale through your nose for 4 counts.",
          "Hold your breath for 4 counts.",
          "Exhale through your mouth for 4 counts.",
          "Hold your breath again for another 4 counts.",
          "Repeat the process for several minutes."
        ]
      },
      {
        "name": "Lion’s Breath",
        "steps": [
          "Sit comfortably with your hands on your knees.",
          "Inhale deeply through your nose.",
          "As you exhale, open your mouth wide and stick out your tongue, stretching it down towards your chin.",
          "While exhaling, make a 'ha' sound from deep within your stomach.",
          "Repeat this process for a few minutes."
        ]
      },
      {
        "name": "Alternate Nostril Breathing",
        "steps": [
          "Sit comfortably and use your right thumb to close off your right nostril.",
          "Inhale deeply through your left nostril.",
          "At the peak of your inhalation, close off your left nostril with your pinkie, then exhale smoothly through your right nostril.",
          "Inhale through your right nostril, then close it off with your thumb.",
          "Exhale through your left nostril.",
          "Continue this pattern for several minutes."
        ]
      },
      {
        "name": "Bhastrika Pranayama",
        "steps": [
          "Sit comfortably with your spine erect.",
          "Take a deep breath in and then exhale forcefully through both nostrils.",
          "Inhale and exhale rapidly, using forceful breaths, for about 10 breaths.",
          "Then, take a deep breath and exhale slowly.",
          "Repeat this process for a few rounds."
        ]
      },
      {
        "name": "Humming Bee Breath (Bhramari)",
        "steps": [
          "Sit comfortably with your eyes closed.",
          "Place your index fingers on your ears.",
          "Inhale deeply and, as you exhale, make a humming sound like a bee.",
          "Continue this for several breaths."
        ]
      }
    ],
    "mindfulness_techniques": [
      {
        "name": "Body Scan",
        "steps": [
          "Lie down comfortably.",
          "Close your eyes and take deep breaths.",
          "Begin at the top of your head and move down through your body.",
          "Notice how each part feels without trying to change anything.",
          "Continue scanning your body down to your feet."
        ]
      },
      {
        "name": "Five Senses Exercise",
        "steps": [
          "Sit comfortably and take a few deep breaths.",
          "Acknowledge five things you can see around you.",
          "Acknowledge four things you can touch.",
          "Acknowledge three things you can hear.",
          "Acknowledge two things you can smell.",
          "Acknowledge one thing you can taste."
        ]
      },
      {
        "name": "Mindful Eating",
        "steps": [
          "Choose a small piece of food, such as a raisin or a nut.",
          "Examine the food closely, noticing its texture and color.",
          "Smell the food and notice any sensations in your mouth or stomach.",
          "Place the food in your mouth, noticing how it feels on your tongue.",
          "Chew the food slowly, being aware of the flavors and textures.",
          "Swallow the food and notice the aftertaste."
        ]
      },
      {
        "name": "Mindful Walking",
        "steps": [
          "Begin walking at a slow pace.",
          "Pay attention to each step, noting the sensation of your foot lifting, moving forward, and making contact with the ground.",
          "Notice the slight swinging motion of your arms as you walk.",
          "Feel the air on your skin and any other sensations.",
          "If your mind wanders, gently bring it back to the act of walking."
        ]
      },
      {
        "name": "Thought Observing",
        "steps": [
          "Sit comfortably and close your eyes.",
          "Instead of trying to stop your thoughts, simply observe them.",
          "Imagine each thought as a cloud passing by in the sky.",
          "Try not to judge or engage with the thoughts, just let them come and go."
        ]
      },
      {
        "name": "Emotion Surfing",
        "steps": [
          "Sit comfortably and close your eyes.",
          "Tune into your emotions without judging or trying to change them.",
          "Imagine riding the wave of the emotion, observing its intensity and duration.",
          "Practice being with the emotion without being overwhelmed by it."
        ]
      },
      {
        "name": "Mindful Listening",
        "steps": [
          "Find a quiet place and close your eyes.",
          "Tune into the sounds around you, both near and far.",
          "Try to identify as many sounds as you can without getting attached to them.",
          "Practice being present with whatever you hear."
        ]
      }
    ],
    "meditation_guidance": [
      {
        "name": "Basic Mindfulness Meditation",
        "steps": [
          "Find a quiet place.",
          "Sit with your back straight.",
          "Focus on your breath, noticing the sensation of inhaling and exhaling.",
          "If your mind wanders, gently bring it back to your breath."
        ]
      },
      {
        "name": "Loving-kindness Meditation",
        "steps": [
          "Sit comfortably and close your eyes.",
          "Begin by sending love and kindness to yourself by repeating: 'May I be happy, may I be well, may I be safe, may I be peaceful and at ease.'",
          "After a few minutes, bring to mind a loved one and send them the same wishes.",
          "Continue this process for neutral people, difficult people, and finally all beings everywhere."
        ]
      },
      {
        "name": "Guided Visualization",
        "steps": [
          "Sit or lie down comfortably.",
          "Listen to a guided meditation or imagine a peaceful place, like a forest or beach.",
          "Engage all your senses in this visualization, noticing sounds, smells, and sensations.",
          "Stay in this place for as long as you'd like, then gently bring yourself back to the present moment."
        ]
      },
      {
        "name": "Mantra Meditation",
        "steps": [
          "Choose a word or phrase that is meaningful to you.",
          "Sit comfortably and repeat the mantra in your mind or out loud.",
          "If your mind wanders, gently bring it back to the mantra.",
          "Continue for as long as you'd like."
        ]
      },
      {
        "name": "Body Scan Meditation",
        "steps": [
          "Lie down comfortably.",
          "Starting from your toes, focus on each part of your body, noticing any sensations.",
          "Move slowly up through your body, all the way to the top of your head.",
          "If your mind wanders, gently bring it back to the part of the body you were focusing on."
        ]
      },
      {
        "name": "Zen Meditation (Zazen)",
        "steps": [
          "Sit on a cushion or chair with your back straight.",
          "Keep your hands in a specific mudra: the left hand palm-up, with the right hand on top of it. The thumbs touch each other, forming an oval shape.",
          "Breathe naturally through your nose.",
          "Keep your eyes open, with your gaze directed downwards, focusing on a spot about 2 to 3 feet in front of you.",
          "If your mind wanders, bring it back to your breath or the sensation of sitting."
        ]
      }
    ]
  }
  
        self._current_cycle = None
        self._templates = [
            "Respond while practicing Diaphragmatic Breathing.",
            "Respond during 4-7-8 Breathing.",
            "Answer while following Box Breathing.",
            "Reply while doing Lion’s Breath.",
            "Respond while trying Alternate Nostril Breathing.",
            "Answer while practicing Bhastrika Pranayama.",
            "Reply while experiencing Humming Bee Breath (Bhramari).",
            "Respond during a Body Scan.",
            "Answer while doing the Five Senses Exercise.",
            "Respond while practicing Mindful Eating.",
            "Reply during Mindful Walking.",
            "Answer while observing your thoughts.",
            "Respond while surfing your emotions.",
            "Reply during Mindful Listening.",
            "Respond during Basic Mindfulness Meditation.",
            "Answer while doing Loving-kindness Meditation.",
            "Respond while visualizing in a Guided Visualization.",
            "Reply while chanting during Mantra Meditation.",
            "Respond while doing a Body Scan Meditation.",
            "Reply during Zen Meditation (Zazen)."
        ]


        self._cycling_templates = cycle(self._templates)

    def select_technique_category(self, category):
        if category not in self._techniques:
            print("Invalid category. Please choose between 'breathing_techniques', 'mindfulness_techniques', or 'meditation_guidance'.")
            return
        self._current_cycle = cycle(self._techniques[category])

    def get_closest_technique(self, user_message, category):
        # Embed the user message
        embedder = Embed4All()
        user_embedding = embedder.embed(user_message)

        # Embed techniques within the chosen category and compute their cosine similarity with user message
        similarities = []
        for technique in self._techniques[category]:
            technique_text = ' '.join(technique["steps"])
            technique_embedding = embedder.embed(technique_text)
            similarity = cosine_similarity([user_embedding], [technique_embedding])
            similarities.append((technique, similarity))

        # Get the technique with the highest similarity within the chosen category
        closest_technique = max(similarities, key=lambda x: x[1])[0]
        print(f"Focusing: {closest_technique['name']}")
        return closest_technique


    def _format_chat_prompt_template(self, category, messages: list) -> str:
        technique = self.get_closest_technique(messages[0]['content'], category) if messages[0]['role'] == "user" else None

        if not technique:
            print("Could not find a suitable technique for the user's message.")
            return

        technique_steps = ' '.join(technique["steps"])

        # System-level instruction
        system_instruction = ("You are a tranquil and centered agent who has just completed a mindfulness technique. "
                            "Grounded in this peaceful state, you are fully prepared and eager to guide, assist, and answer questions. "
                            "Every response you provide is influenced by the meditation, breathing, or mindfulness technique you've just practiced.")

        # Combine the system instruction, the technique's instructions, and the conversation history to form the full prompt
        full_prompt = f"{system_instruction}\n\n{technique_steps}"  
        print(f"Prompt: {full_prompt}")
        for message in messages:
            if message["role"] == "user":
                user_message = f"\n\nUSER: {message['content']}\n"
                full_prompt += user_message
            if message["role"] == "assistant":
                assistant_message = f"ASSISTANT: {message['content']}\n"
                full_prompt += assistant_message

        tokens = []
        for token in self.model.generate(full_prompt, max_tokens=2048, streaming=True):
            tokens.append(token)

        return ''.join(tokens)


    def start_conversation(self):
            while True:
                print("Choose a technique category: 'breathing', 'mindfulness', or 'meditation'. Type 'exit' to quit.")
                category_choice = input().strip().lower()
                
                if category_choice == "exit":
                    break
                
                if category_choice not in ["breathing", "mindfulness", "meditation"]:
                    print("Invalid choice. Please choose a valid category or type 'exit' to quit.")
                    continue
                
                # Map user's choice to our technique dictionary keys
                category_map = {
                    "breathing": "breathing_techniques",
                    "mindfulness": "mindfulness_techniques",
                    "meditation": "meditation_guidance"
                }
                
                self.select_technique_category(category_map[category_choice])
                
                print("Enter your message (or type 'exit' to quit):")
                user_message = input().strip()
                
                if user_message.lower() == "exit":
                    break
                
                response = self._format_chat_prompt_template(category_map[category_choice], [{"role": "user", "content": user_message}])

                print(response)


# Example usage:
rotating_template = TechniqueRotatingTemplateGPT4All("orca-mini-3b.ggmlv3.q4_0.bin")
rotating_template.start_conversation()
