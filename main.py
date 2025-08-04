from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
async def welcome_page():
    return {"message": "Hesap Makinesi Uygulamasına Hoş Geldiniz!"}

class CalculationRequest(BaseModel):
    operation: str
    number1: float
    number2: float

@app.post("/calculate")
async def calculate(request: CalculationRequest):
    if request.operation == "+":
        result = request.number1 + request.number2
    elif request.operation == "-":
        result = request.number1 - request.number2
    elif request.operation == "*":
        result = request.number1 * request.number2
    elif request.operation == "/":
        if request.number2 == 0:
            raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Bölme işlemi için ikinci sayı sıfır olamaz.")
        result = request.number1 / request.number2
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Geçersiz işlem. Lütfen '+', '-', '*' veya '/' kullanın.")
    
    return {"İşlem Sonucu": result}
