# Quiz Game

score = 0

questions = [
    {
        "question": "1. What is the capital of India?",
        "options": ["A. Delhi", "B. Mumbai", "C. Chennai", "D. Kolkata"],
        "answer": "A"
    },
    {
        "question": "2. Which language is used for Artificial Intelligence?",
        "options": ["A. HTML", "B. Python", "C. CSS", "D. XML"],
        "answer": "B"
    },
    {
        "question": "3. Who is known as the Father of Computers?",
        "options": ["A. Charles Babbage", "B. Albert Einstein", "C. Newton", "D. Bill Gates"],
        "answer": "A"
    },
    {
        "question": "4. Which planet is called the Red Planet?",
        "options": ["A. Earth", "B. Jupiter", "C. Mars", "D. Venus"],
        "answer": "C"
    },
    {
        "question": "5. Which keyword is used to define a function in Python?",
        "options": ["A. function", "B. def", "C. define", "D. fun"],
        "answer": "B"
    }
]

print("========== PYTHON QUIZ GAME ==========")
print("Type A, B, C or D\n")

for q in questions:
    print(q["question"])

    for option in q["options"]:
        print(option)

    user_answer = input("Your Answer: ").upper()

    if user_answer == q["answer"]:
        print("✅ Correct!\n")
        score += 1
    else:
        print(f"❌ Wrong! Correct Answer: {q['answer']}\n")

print("========== RESULT ==========")
print(f"Your Score: {score}/{len(questions)}")

percentage = (score / len(questions)) * 100

print(f"Percentage: {percentage:.2f}%")

if percentage >= 80:
    print("Grade: A+")
elif percentage >= 60:
    print("Grade: A")
elif percentage >= 40:
    print("Grade: B")
else:
    print("Grade: C")