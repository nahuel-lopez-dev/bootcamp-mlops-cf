from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from openai import OpenAI
import os

# Cargar la variable de entorno
api_key = os.getenv("OPENAI_API_KEY")

# Crear el cliente con la clave de API
client = OpenAI(api_key=api_key)

app = FastAPI()

templates = Jinja2Templates(directory="templates")

@app.get("/", response_class=HTMLResponse)
async def get_chatbot(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "user_message": None, "ai_message": None})

@app.post("/chat", response_class=HTMLResponse)
async def post_chatbot(request: Request, user_message: str = Form(...)):
    try:
        response = client.chat.completions.create(model="gpt-3.5-turbo",
        messages=[
            {"role": "user", "content": user_message}
        ],
        max_tokens=150,
        temperature=0.7)
        ai_message = response.choices[0].message.content.strip()
    except Exception as e:
        ai_message = f"Error: {str(e)}"

    return templates.TemplateResponse("index.html", {
        "request": request,
        "user_message": user_message,
        "ai_message": ai_message
    })
