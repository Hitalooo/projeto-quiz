from pydantic import BaseModel
from typing import List

class Question(BaseModel):
    id: str
    text: str
    options: List[str]
    correct_answer: str

questions_multiple_choice = [
    Question(id="q1", text="Qual a capital do Brasil?", options=["Rio", "Brasília", "São Paulo"], correct_answer="Brasília"),
    Question(id="q2", text="Qual o maior planeta do sistema solar?", options=["Terra", "Marte", "Júpiter"], correct_answer="Júpiter"),
]

questions_true_false = [
    Question(id="q3", text="O Sol é uma estrela.", options=["Verdadeiro", "Falso"], correct_answer="Verdadeiro"),
    Question(id="q4", text="2 + 2 = 5", options=["Verdadeiro", "Falso"], correct_answer="Falso"),
]
