class Brain():

    def __init__(self, q_list):
        self.question_number = 0
        self.question_list = q_list
        self.score = 0

    def still_have_question(self):
        if self.question_number < len(self.question_list):
            return True
        else:
            print("No more question")
            return False

    def next_question(self):
        question = self.question_list[self.question_number]

        print(f"Q{self.question_number+1} {question}")
        asw = input("True / False:")

        if asw == question.answer:
            print("You got it right!")
            self.score += 1
        else:
            print("That's wrong")

        print("The correct answer:", question.answer)
        print(f"Your currenct score: {self.score}/{self.question_number+1}")
        self.question_number += 1

