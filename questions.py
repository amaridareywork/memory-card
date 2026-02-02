from random import shuffle


class Question:
    def __init__(self, question: str, right_answer: str, wrong1: str, wrong2: str, wrong3: str) -> None:
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3


class Questions:
    def __init__(self) -> None:
        self.list_of_questions = []
        self.current_question = -1

    def shuffle_question(self):
        shuffle(self.list_of_questions)
    
    def add_question(self, question: str, right_answer: str, wrong1: str, wrong2: str, wrong3: str) -> None:
        self.list_of_questions.append(Question(question, right_answer, wrong1, wrong2, wrong3))
    
    def get_current_question(self) -> Question:
        return self.list_of_questions[self.current_question]
    
    def next_question(self) -> Question:
        self.current_question += 1
        if self.current_question == len(self.list_of_questions): self.current_question = 0
        return self.list_of_questions[self.current_question]
    
    def next_question_random(self) -> tuple:
        self.current_question += 1
        if self.current_question == len(self.list_of_questions): self.current_question = 0
        question = self.list_of_questions[self.current_question]
        random_answer = [question.right_answer, question.wrong1, question.wrong2, question.wrong3]
        shuffle(random_answer)

        return question.question, question.right_answer, random_answer
