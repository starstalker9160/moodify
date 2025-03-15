from google import genai

dict={
    'happy':0,
    'sad':6,
    'angry':6,
    'excited':0,
    'scared':5,
    'anxious':2,
}

def get_advice(dict):
    emotions = sorted(dict, key=dict.get, reverse=True)[:2]

    prompt = f'I am feeling {emotions[0]} and {emotions[1]}. Give me advice to feel better. In 2-3 paragraphs'

    client = genai.Client(api_key="AIzaSyDNEZphU1r8peEA84nPCMlSn_48hxwQrBY")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

get_advice(dict)