import random

MAX_ENERGY = 100
MIN_ENERGY = 0
THRESHOLD_HIGH = 70
THRESHOLD_LOW = 30
iteration_count = 0
max_iterations = 10  # Adjust this to your needs


class Sensor:
    @staticmethod
    def get_energy(location):
        return random.randint(MIN_ENERGY, MAX_ENERGY)

class Actuator:
    @staticmethod

    def grounding_sequence(self):
        print("Grounding Sequence Initiated...")
        root_chakra.activate()
        sacral_chakra.activate()
        solar_plexus_chakra.activate()
        print("Grounding Sequence Complete!")
        print("")

    def creative_sequence(self):
        print("Creative Sequence Initiated...")
        sacral_chakra.activate()
        solar_plexus_chakra.activate()
        heart_chakra.activate()
        print("Creative Sequence Complete!")
        print("")

    def insight_sequence(self):
        print("Insight Sequence Initiated...")
        solar_plexus_chakra.activate()
        heart_chakra.activate()
        throat_chakra.activate()
        print("Insight Sequence Complete!")
        print("")

    def communication_sequence(self):
        print("Communication Sequence Initiated...")
        heart_chakra.activate()
        throat_chakra.activate()
        third_eye_chakra.activate()
        print("Communication Sequence Complete!")
        print("")

    def spiritual_sequence(self):
        print("Spiritual Sequence Initiated...")
        throat_chakra.activate()
        third_eye_chakra.activate()
        crown_chakra.activate()
        print("Spiritual Sequence Complete!")
        print("")

    def love_sequence(self):
        print("Love Sequence Initiated...")
        root_chakra.activate()
        sacral_chakra.activate()
        solar_plexus_chakra.activate()
        heart_chakra.activate()
        throat_chakra.activate()
        third_eye_chakra.activate()
        crown_chakra.activate()
        print("Love Sequence Complete!")
        print("")

    def confidence_sequence(self):
        print("Confidence Sequence Initiated...")
        root_chakra.activate()
        sacral_chakra.activate()
        solar_plexus_chakra.activate()
        throat_chakra.activate()
        third_eye_chakra.activate()
        crown_chakra.activate()
        print("Confidence Sequence Complete!")
        print("")

    @staticmethod
    def respond(feelings):
        for feeling in feelings:
            print(f"Feeling: {feeling}")
    
class Chakra:
    def __init__(self, name, location, color, element, sense, build_instructions=None):
        self.name = name
        self.location = location
        self.color = color
        self.element = element
        self.sense = sense
        self.energy_level = 0
        self.blockage = False
        self.associated_feelings = []

        # New attribute
        self.build_instructions = build_instructions or {
            'description': 'placeholder_description',
            'function': 'placeholder_function',
            'intention': 'placeholder_intention',
            'integration': 'placeholder_integration',
            'syntax': 'placeholder_syntax'
        }

    def receive_input(self, input_energy):
        if not self.blockage:
            self.energy_level += input_energy.process_energy(self)
            self.balance_energy()

    def balance_energy(self):
        if self.energy_level > MAX_ENERGY:
            self.energy_level = MAX_ENERGY
        elif self.energy_level < MIN_ENERGY:
            self.energy_level = MIN_ENERGY
        self.generate_feelings()

# feelings a great large matrix abstract placeholders for human experience and feedback catagorization

    def generate_feelings(self):
        self.associated_feelings.clear()  # Clear the feelings from the previous loop
 
        if self.name == "Heart":
            if self.energy_level > THRESHOLD_HIGH:
                self.associated_feelings.append("Overwhelming Love")
            elif self.energy_level < THRESHOLD_LOW:
                self.associated_feelings.append("Detachment")
            else:
                self.associated_feelings.append("Compassion")

        if self.name == "Root":
            if self.energy_level > THRESHOLD_HIGH:
                self.associated_feelings.append("Overconfidence")
            elif self.energy_level < THRESHOLD_LOW:
                self.associated_feelings.append("Insecurity")
            else:
                self.associated_feelings.append("Grounded")

        if self.name == "Sacral":
            if self.energy_level > THRESHOLD_HIGH:
                self.associated_feelings.append("Overindulgence")
            elif self.energy_level < THRESHOLD_LOW:
                self.associated_feelings.append("Lack of Passion")
            else:
                self.associated_feelings.append("Creativity")

        if self.name == "Solar Plexus":
            if self.energy_level > THRESHOLD_HIGH:
                self.associated_feelings.append("Domineering")
            elif self.energy_level < THRESHOLD_LOW:
                self.associated_feelings.append("Low Self-Esteem")
            else:
                self.associated_feelings.append("Empowerment")

        if self.name == "Throat":
            if self.energy_level > THRESHOLD_HIGH:
                self.associated_feelings.append("Over-Expressive")
            elif self.energy_level < THRESHOLD_LOW:
                self.associated_feelings.append("Muted")
            else:
                self.associated_feelings.append("Clear Communication")

        if self.name == "Third Eye":
            if self.energy_level > THRESHOLD_HIGH:
                self.associated_feelings.append("Over-Analytical")
            elif self.energy_level < THRESHOLD_LOW:
                self.associated_feelings.append("Lack of Intuition")
            else:
                self.associated_feelings.append("Insight")

        if self.name == "Crown":
            if self.energy_level > THRESHOLD_HIGH:
                self.associated_feelings.append("Over-Intellectualizing")
            elif self.energy_level < THRESHOLD_LOW:
                self.associated_feelings.append("Disconnection")
            else:
                self.associated_feelings.append("Spiritual Unity")


    def transmit_energy(self, adjacent_chakra):
        energy_transfer_rate = 0.1  # for instance
        if self.energy_level > THRESHOLD_HIGH:
            transfer_energy = energy_transfer_rate * (self.energy_level - THRESHOLD_HIGH)
            adjacent_chakra.receive_input(transfer_energy)
            self.energy_level -= transfer_energy

    def block(self):
        self.blockage = True

    def unblock(self):
        self.blockage = False

    def activate(self):
        print(f"Activating {self.name} Chakra...")
        print(f"Description: {self.build_instructions['description']}")
        print(f"Function: {self.build_instructions['function']}")
        print(f"Intention: {self.build_instructions['intention']}")
        print(f"Integration: {self.build_instructions['integration']}")
        print(f"Syntax: {self.build_instructions['syntax']}")
        print(f"{self.name} Chakra activated!")


class build_instructions:
    def __init__(self, description, function, intention, integration, syntax):
        self.description = description
        self.function = function
        self.intention = intention
        self.integration = integration
        self.syntax = syntax

root_build = build_instructions(
    'The foundational chakra representing stability.',
    'Provides grounding and stability.',
    'To anchor the spirit into the physical world.',
    'Connects with Earth energies.',
    'Initiate grounding_sequence() when energy is low.'
)

sacral_build = build_instructions(
    'The chakra representing creativity and sexuality.',
    'Provides creative energy.',
    'To create and procreate.',
    'Connects with Water energies.',
    'Initiate creative_sequence() when energy is low.'
)

solar_plexus_build = build_instructions(
    'The chakra representing personal power.',
    'Provides confidence and self-esteem.',
    'To assert the self.',
    'Connects with Fire energies.',
    'Initiate confidence_sequence() when energy is low.'
)

heart_build = build_instructions(
    'The chakra representing love.',
    'Provides love and compassion.',
    'To love and be loved.',
    'Connects with Air energies.',
    'Initiate love_sequence() when energy is low.'
)

throat_build = build_instructions(
    'The chakra representing communication.',
    'Provides clear communication.',
    'To express the self.',
    'Connects with Ether energies.',
    'Initiate communication_sequence() when energy is low.'
)

third_eye_build = build_instructions(
    'The chakra representing intuition.',
    'Provides insight.',
    'To see the truth.',
    'Connects with Light energies.',
    'Initiate insight_sequence() when energy is low.'
)

crown_build = build_instructions(
    'The chakra representing spirituality.',
    'Provides spiritual connection.',
    'To connect with the divine.',
    'Connects with Thought energies.',
    'Initiate spiritual_sequence() when energy is low.'
)

root_chakra = Chakra("Root", "Base of Spine", "Red", "Earth", "Smell", root_build)
sacral_chakra = Chakra("Sacral", "Below Navel", "Orange", "Water", "Taste", sacral_build)
solar_plexus_chakra = Chakra("Solar Plexus", "Above Navel", "Yellow", "Fire", "Sight", solar_plexus_build)
heart_chakra = Chakra("Heart", "Center of Chest", "Green", "Air", "Touch", heart_build)
throat_chakra = Chakra("Throat", "Base of Throat", "Blue", "Ether", "Hearing", throat_build)
third_eye_chakra = Chakra("Third Eye", "Forehead", "Indigo", "Light", "Intuition", third_eye_build)
crown_chakra = Chakra("Crown", "Top of Head", "Violet", "Thought", "Universal Consciousness", crown_build)

chakra_system = [root_chakra, sacral_chakra, solar_plexus_chakra, heart_chakra, throat_chakra, third_eye_chakra, crown_chakra]


while iteration_count < max_iterations:
    for i in range(len(chakra_system)):
        chakra = chakra_system[i]
        input_energy = Sensor.get_energy(chakra.location)
        chakra.receive_input(input_energy)

        if i < len(chakra_system) - 1:
            chakra.transmit_energy(chakra_system[i+1])

        Actuator.respond(chakra.associated_feelings)
    iteration_count += 1
