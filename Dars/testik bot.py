class Test:
    def __init__(self, title):
        self.title = title
        self.questions = []

    def add_question(self, question):
        self.questions.append(question)

    def save_test(self):
        with open(f"{self.title}.txt", "w") as file:
            for question in self.questions:
                file.write(question)
                file.close()

class Question:
    def __init__(self, prompt, options, correct_answer):
        self.prompt = prompt
        self.options = options
        self.correct_answer = correct_answer

    def check_answer(self, answer):
        return answer == self.correct_answer


test = Test("MyTest")

# Test 1
question1 = Question("What is the capital of France?\n",
                        ["a) London", "b) Paris", "c) Rome", "d) Madrid"],
                        "b")
test.add_question(question1)

# Test 2
question2 = Question("What is 2 + 2?\n",
                        ["a) 3", "b) 4", "c) 5", "d) 6"],
                        "b")
test.add_question(question2)

test.save_test()
