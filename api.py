from models import questions_multiple_choice, questions_true_false

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

def solicitar_revisao(question_id: str, motivo: str):
    revisoes.append({
        "question_id": question_id,
        "motivo": motivo
    })
    return "Revisão solicitada com sucesso!"
