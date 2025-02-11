import json

with open("questions.json","r") as file:
    content = file.read()

data = json.loads(content)

#print(content)
#print(type(content))
#print(data)
#print(type(data))

score = 0 
result = []

name = input("What's your name?")
print(f"Hi {name}! Let's start \n")

for index, question in enumerate(data):
    #print(type(question))
    print(f"\nQ{index+1}) {question['question_text']} \n")
    for index, option in enumerate(question["options"]):
        print(f"{index+1} - {option}")
    
    user_choice = int(input("\n"+"Enter your answer: "))
    question["user_choice"] = user_choice

    if question["correct_answer"] == user_choice:
        score = score + 1
        result.append(True)
    else:
        result.append(False)
#print(data)
print(f"You got {score} questions out of {len(data)} right!")
print(score)
print(result)


