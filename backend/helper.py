from google import genai
import os, sys, time, shutil, random


def foreplay() -> str:
    """Initialization of the app, (foreplay before the good stuff)
        1. Create db if not existing
        2. Clear pycache to avoid bugs
    """
    filepath = "db/moodJournal.csv"
    folder = os.path.dirname(filepath)

    out = "I-"

    if not os.path.exists(folder):
        os.makedirs(folder)
        out += "2"
    else:
        out += "1"

    if not os.path.exists(filepath):
        with open(filepath, "w") as file:
            file.write("S,Rating,Happy,Anger\n")
        out += "2"
    else:
        out += "1"

    pycache_path = os.path.join(os.getcwd(), "backend/__pycache__")
    if os.path.exists(pycache_path):
        shutil.rmtree(pycache_path)
    
    return out


def handle(d: dict) -> None:
    try:
        prompt = f"""
            You are an advice bot in a mood journal app, the user has entered their feelings such that:
                - happy, on a scale of 1 to 5 where 1 means crying and 5 means elated: {d["happy"]}
                - angry, on a scale of 1 to 5 where 1 means calm and 5 means fuming: {d["anger"]}
                - anxiety, on a scale of 1 to 5 where 1 means none at all and 5 means near vomiting: {d["anxiousness"]}
            Give me advice in one paragraph no longer than 100 words
            Do not hallucinate, do not make up facts, be kind and talk soothingly.
        """

        client = genai.Client(api_key="AIzaSyDNEZphU1r8peEA84nPCMlSn_48hxwQrBY")
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=prompt
        )
        
        print(response.text)
    except Exception as e:
        print(f"Error generating response: {e}")
