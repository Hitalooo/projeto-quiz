from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict, List
from models import questions_multiple_choice, questions_true_false, RespostaRequest, RevisaoRequest

app = FastAPI()
revisoes = []

def listar_questoes(tipo: str):
    if tipo == "multiple":
        return questions_multiple_choice
    elif tipo == "truefalse":
        return questions_true_false
    else:
        return []

def corrigir_quiz(tipo: str, respostas_usuario: dict):
    if tipo == "multiple":
        perguntas = questions_multiple_choice
    else:
        perguntas = questions_true_false

    score = 0
    feedback = []

    for q in perguntas:
        user_answer = respostas_usuario.get(q.id)
        correct = user_answer == q.correct_answer
        if correct:
            score += 1
        feedback.append({
            "question": q.text,
            "user_answer": user_answer,
            "correct_answer": q.correct_answer,
            "is_correct": correct
        })

    return {"score": score, "total": len(perguntas), "feedback": feedback}

@app.get("/quizzes/{tipo}/perguntas")
def api_listar_questoes(tipo: str):
    perguntas = listar_questoes(tipo)
    if not perguntas:
        raise HTTPException(status_code=404, detail="Tipo de quiz não encontrado")
    resultado = []
    for q in perguntas:
        resultado.append({
            "id": q.id,
            "text": q.text,
            "options": q.options
        })
    return resultado

@app.post("/quizzes/{tipo}/corrigir")
def api_corrigir_quiz(tipo: str, respostas: RespostaRequest):
    perguntas = listar_questoes(tipo)
    if not perguntas:
        raise HTTPException(status_code=404, detail="Tipo de quiz não encontrado")
    resultado = corrigir_quiz(tipo, respostas.answers)
    return resultado

@app.post("/quizzes/revisoes")
def api_solicitar_revisao(dados: RevisaoRequest):
    revisoes.append({
        "question_id": dados.question_id,
        "motivo": dados.motivo
    })
    return {"message": "Revisão solicitada com sucesso!"}
