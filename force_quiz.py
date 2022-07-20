import json

user_score = 0
questions = {}

print("Hello there! I'm Obi-Wan Kenobi - what is your name?")
name = input("Name: ")
print(" ")
print("Hello " + str(
    name) + ", I will be asking you some questions today to determine if you are closer to the light or dark side of the force and whose padawan you should become.")
print(" ")
print("Are you ready?")
print("Please answer with YES or NO: ")
response = input()

if response.lower() == 'yes':
    print("Alright then.")
    print(" ")
elif response.lower() == 'no':
    print("")
    print("May the Force be with you!.")
    exit()

with open('./force_q.json') as f:
    questions = json.load(f)

for question in questions:
    possible_inputs = []
    answers = questions[question]['answers']
    try:
        message_on_input = questions[question]['message_on_input'] or "your answer: "
    except KeyError:
        message_on_input = "your answer: "

    if response.lower() == 'yes':
        print()
        print(question)
        print()
    elif response.lower() == 'no':
        print("May the Force be with you!.")

    for count, answer in enumerate(answers):
        score = questions[question]['answers'][answer]
        possible_inputs.append((str(count), answer))
        print(f"{count})    {answer.capitalize()}")
    while True:
        user_answer = input(message_on_input).lower()
        is_answer_valid = user_answer in [item for sublist in possible_inputs for item in sublist]
        if is_answer_valid:
            score = [t[0] for t in possible_inputs if t[0] == user_answer or t[1] == user_answer]
            answer_picked = [t[1] for t in possible_inputs if t[0] == user_answer or t[1] == user_answer]
            add_to_score = questions[question]['answers'][answer_picked[0]]
            if is_answer_valid:
                user_score += add_to_score
            break
        else:
            print(f"answer '{user_answer}' not found, try again")
print(" ")
print("Data processing...BIP...BIP...")
print("")
print(f"score: {user_score}")
print("")

if int(user_score) >= 10:
    if int(user_score) <= 24:
        print("The light side of the force is strong in you " + name + ", your master should be Luke Skywalker")
if int(user_score) >= 25:
    if int(user_score) <= 35:
        print("The light side of the force is strong in you " + name + ", your master should be Kid Fisto")
if int(user_score) >= 36:
    if int(user_score) <= 43:
        print("The light side of the force is strong in you " + name + ", your master should be Qui-Gon Jinn")
if int(user_score) >= 44:
    if int(user_score) <= 55:
        print("The light side of the force is strong in you " + name + ", your master should be Ashoka Tano")
if int(user_score) >= 56:
    if int(user_score) <= 63:
        print("The light side of the force is strong in you " + name + ", your master should be Mace Windu")
if int(user_score) >= 64:
    if int(user_score) <= 82:
        print("The light side of the force is strong in you " + name + ", your master should be Plo Koon")
if int(user_score) >= 83:
    if int(user_score) <= 109:
        print("The light side of the force is strong in you " + name + ", your master should be Yoda")

if int(user_score) >= 123:
    if int(user_score) <= 133:
        print("The light side of the force is strong in you " + name + ", your master should be Darth Vader")
if int(user_score) >= 134:
    if int(user_score) <= 144:
        print("The light side of the force is strong in you " + name + ", your master should be Kylo Ren")
if int(user_score) >= 145:
    if int(user_score) <= 152:
        print("The light side of the force is strong in you " + name + ", your master should be Count Dooku")
if int(user_score) >= 153:
    if int(user_score) <= 162:
        print("The light side of the force is strong in you " + name + ", your master should be Asajj Ventress")
if int(user_score) >= 163:
    if int(user_score) <= 170:
        print("The light side of the force is strong in you " + name + ", your master should be Darth Vader")
if int(user_score) >= 171:
    if int(user_score) <= 179:
        print("The light side of the force is strong in you " + name + ", your master should be Lord Bane")
if int(user_score) >= 180:
    if int(user_score) <= 219:
        print("The light side of the force is strong in you " + name + ", your master should be Imperator Palpatin")
