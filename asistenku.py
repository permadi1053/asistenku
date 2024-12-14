import requests
import json

Gemini_Api_Key= "your Gemini API Key "
Endpoint_Url = "https://generativelanguage.googleapis.com/v1/models/"
Gemini_Model = "gemini-1.5-flash"

def gemini_ai (text):
    
    api_url = f"{Endpoint_Url}{Gemini_Model}:generateContent"
    url = f"{api_url}?key={Gemini_Api_Key}"
     
    headers = {
        "Content-Type": "application/json"
    }

    
    request_body = {
        "contents": [
            {
                "parts": [
                    {
                        "text": text
                    }
                ]
            }
        ]
    }

    response = requests.post(url, headers=headers, data=json.dumps(request_body))
    
    response_data = response.json()
    answer = response_data.get('candidates', [{}])[0].get('content', {}).get('parts', [{}])[0].get('text', "Asisten tidak menjawab!")
    return answer


def chatbot():
    print ("AsistenKu - Ketik 'exit' untuk keluar")
    while True:
        user_input= input("anda: ")
        if user_input.lower() == "exit":
            print ("Keluar dari Asistenku, Terimakasih!")
            break
        response = gemini_ai(user_input)
        print(f"Asisten: {response}")
        
chatbot()
