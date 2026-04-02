import google.generativeai as genai

genai.configure(api_key="AIzaSyB57M1tiZuIJmb2-pnMjNGZ2dT-6VMS9Z0")
for m in genai.list_models():
    print(m.name)