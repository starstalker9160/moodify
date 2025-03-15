from google import genai

dict_ = sorted({
    "happy-sad": 0,
    "angry-calm": 6,
})

def get_advice(moodDict):
    prompt = f"""
        You are an advice bot in a mood journal app, the user has entered their feelings such that:
            - on a scale of happy to sad where happy is 10 they feel: {moodDict[0]}
            - on a scale of angry to calm where angry is 10 they feel: {moodDict[1]}
        Give me advice in one paragraph no longer than 60 words
        Do not hallucinate, do not make up facts, be kind and talk soothingly.
    """

    client = genai.Client(api_key="AIzaSyDNEZphU1r8peEA84nPCMlSn_48hxwQrBY")
    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=prompt
    )
    return response.text

print(get_advice(dict_))