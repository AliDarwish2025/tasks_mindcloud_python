qa_data = {
    "how are you": "I'm good, thanks for asking!",
    "what's your name": "I'm just a test bot made in Python.",
    "who made you": "Some programmer made me as part of a learning thing."
}

user_name = None

print("Hey! I'm your bot, type 'exit' to stop talking.")

while True:
    user_input = input("You: ").strip()

    if user_input.lower() == "exit":
        print("see ya!")
        break

    if "my name is" in user_input or "i am" in user_input:
        name = user_input.split()[-1]
        if user_name is None:
            user_name = name
            print(f"hey {user_name}, nice meetin u!")
        else:
            print(f"yo {user_name}, we meet again!")
        continue

    if "+" in user_input:
        parts = user_input.split("+")
        try:
            num1 = int(parts[0].strip())
            num2 = int(parts[1].strip())
            result = num1 + num2
            print("result:", result)
        except ValueError:
            print("hmm.. write real numbers pls")
        continue

    if "-" in user_input:
        parts = user_input.split("-")
        try:
            num1 = int(parts[0].strip())
            num2 = int(parts[1].strip())
            result = num1 - num2
            print("result:", result)
        except ValueError:
            print("hmm.. write real numbers pls")
        continue

    if user_input in qa_data:
        print(qa_data[user_input])
    else:
        print("no clue what that means")
        new_answer = input("wanna teach me? (yes/no): ").strip().lower()
        if new_answer == "yes":
            answer = input("type it here: ").strip()
            qa_data[user_input] = answer
            print("got it, will remember!")
