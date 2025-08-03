# Documentação do Projeto: Plataforma de quiz

## 1. Visão Geral

**Tecnologias Utilizadas:**

- Python
- FastAPI
- Uvicorn

**Descrição:**  
Implementação de uma plataforma de quizzes online para estudos, com perguntas de múltipla escolha e verdadeiro ou falso, correção automática e solicitação de revisão.

**Objetivo:**  
Proporcionar uma ferramenta interativa de aprendizado que permita aos usuários testar seus conhecimentos, acompanhar sua pontuação e contribuir com feedback sobre o conteúdo.

---

## 2. Descrição Detalhada do Projeto

### O que é o projeto?

 A aplicação consiste em uma plataforma de quizzes online, com foco em estudos. Os quizzes serão intuitivos, com perguntas de múltipla escolha e verdadeiro ou falso. Ao final de cada quiz, será exibida a pontuação obtida, permitindo ao usuário acompanhar seu progresso. A plataforma também permitirá que o usuário solicite uma revisão de perguntas ou respostas que considerar incorretas ou incompletas. Essa solicitação será enviada para o administrador ou moderador do sistema, que poderá analisar e, se necessário, corrigir a questão. Para acessar o sistema e suas funcionalidades, será necessário realizar login ou cadastro.

### 2.1 Funcionalidades Principais

- **Funcionalidade 01:** Realizar quizzes de múltipla escolha
- **Funcionalidade 02:** Realizar quizzes de verdadeiro ou falso
- **Funcionalidade 03:** Exibir pontuação ao final do quiz
- **Funcionalidade 04:** Permitir revisão de quizzes realizados
- **Funcionalidade 05:** Permitir solicitação de revisão de perguntas ou respostas

### 2.2 Arquitetura do Código

A arquitetura do código é organizada da seguinte maneira:

```plaintext
projeto-quiz/
├── scripts/
├── templates/         
├── static/
├── main.py             # Ponto de entrada (inicialização)
├── models.py           # Modelos com Pydantic
├── requirements.txt    # Bibliotecas necessárias para executar o projeto
```

## 3. Etapas de Entrega (Cronograma Detalhado)

- **Etapa 1:** Levantar requisitos e realizar o planejamento inicial.
- **Etapa 2:** Desenvolver a API com as funcionalidades básicas.
- **Etapa 3:** Integrar a API com o banco de dados.
- **Etapa 4:** Realizar testes e ajustes necessários.
- **Etapa 5:** Realizar o deploy da aplicação e entrega final.

