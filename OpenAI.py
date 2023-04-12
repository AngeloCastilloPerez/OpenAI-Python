#Una vez instalaste Open AI, estas listo para continuar:
#Primero importamos OpenAI

import openai
# Indica el API Key
openai.api_key = "INGRESA TU KEY"
# Uso de ChapGPT en Python
model_engine = "text-davinci-003"
prompt = "INGRESA TU PROMP"
completion = openai.Completion.create(engine=model_engine,
                                    prompt=prompt,
                                    max_tokens=1024,
                                    n=1,
                                    stop=None,
                                    temperature=0.7)
respuesta=""
for choice in completion.choices:
    respuesta=respuesta+choice.text
    print(f"Response: %s" % choice.text)