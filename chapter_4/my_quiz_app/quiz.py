
import random
from utils import load_txt_questions, load_csv_questions



def ask_text_question(q):
    """
    Display q['prompt'] and return True if the player’s typed answer,
    stripped of spaces and case-normalized, matches q['answer'].
    """
    user = input(q["prompt"] + " ")
    return user.strip().lower() == q["answer"].lower()


def ask_mc_question(q):
    """
    Print q['prompt'] and its options numbered 1–3.
    Loop until the user types “1”, “2”, or “3”, then check
    if the chosen option matches q['answer'] (case-insensitive).
    """
    # 1) Show prompt and options
    print(q["prompt"])
    for idx, opt in enumerate(q["options"], start=1):
        print(f"  {idx}) {opt}")

    # 2) Prompt until valid choice
    while True:
        choice = input("Your choice (1-3): ")
        if choice in ("1", "2", "3"):
            selected = q["options"][int(choice) - 1]
            # 3) Compare normalized text
            return selected.lower() == q["answer"].lower()
        print("Please enter 1, 2, or 3.")




def run_quiz():
    # 1) Load and combine questions
    questions = load_txt_questions() + load_csv_questions()

    # 2) Shuffle so order is random each play
    random.shuffle(questions)

    # 3) Initialize score counter
    score = 0

    # 4) Ask every question in turn
    for q in questions:
        # 4a) Pick the right ask-function
        if q["options"] is None:
            correct = ask_text_question(q)
        else:
            correct = ask_mc_question(q)

        # 4b) Provide feedback and update score
        if correct:
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Incorrect. The answer was: {q['answer']}\n")

    # 5) Compute total questions and show summary

    total = len(questions)

      # 1) Raw summary
    print(f"Quiz complete! You scored {score}/{total} ({score/total:.0%}).")

     # 2) Custom feedback
    print(give_feedback(score, total))


def give_feedback(score, total):
    """
    Return a little badge and message based on the player’s percentage.
    """
    percentage = score / total

    if percentage == 1.0:
        return "🏆 Perfect score! You’re a quiz master!"
    elif percentage >= 0.9:
        return "🎉 Great job! Almost perfect!"
    elif percentage >= 0.7:
        return "👍 Good work! You know your stuff."
    elif percentage >= 0.5:
        return "🙂 Not bad—keep practicing!"
    else:
        return "🤔 Don’t worry, try again to improve."
    


if __name__ == "__main__":
    run_quiz()



