import os, shutil
from google import genai
from backend.secrets import token


def initialize() -> str:
    """Initialization of the app
        1. Create db if not existing
        2. Clear pycache to avoid bugs
    """
    filepath = "static/db/moodJournal.csv"
    folder = os.path.dirname(filepath)

    out = "I-"

    if not os.path.exists(folder):
        os.makedirs(folder)
        out += "2"
    else:
        out += "1"

    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write("S,Happy,Anger,Anxiety\n")
        out += "2"
    else:
        out += "1"

    pycache_path = os.path.join(os.getcwd(), "backend/__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)

    return out


def handle(d: dict) -> None:
    """Generate AI Response based on data"""
    if d == None:
        return None

    try:
        prompt = f"""
            You are an advice bot in a mood journal app, the user has entered their feelings such that:
                - happy, on a scale of 1 to 5 where 1 means crying and 5 means elated: {d["happy"]}
                - angry, on a scale of 1 to 5 where 1 means calm and 5 means fuming: {d["anger"]}
                - anxiety, on a scale of 1 to 5 where 1 means none at all and 5 means near vomiting: {d["anxiousness"]}
            Give me advice in one two paragraphs, first one acknowledging their feeligns (no more than 30 words)
            and second one (no more than 50 words) giving actionable advice to better their mood, or if they're already
            really happy then to spread that happiness to the peopl around them.
            Respond in plain text, no markdown formatting, do not hallucinate, do not make up facts, be kind and talk
            soothingly.
        """

        client = genai.Client(api_key=token)
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )

        return response.text
    except Exception as e:
        print(f"Error generating response: {e}")
