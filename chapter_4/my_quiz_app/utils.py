
import csv

def load_txt_questions(path="questions.txt"):
    
    questions = []
    with open(path, "r", encoding="utf-8") as f:
        for raw in f:
            line = raw.strip()
            if not line or "|" not in line:
                continue
            prompt, answer = [part.strip() for part in line.split("|", 1)]
            questions.append({
                "prompt": prompt,
                "options": None,
                "answer": answer
            })
    return questions



def load_csv_questions(path="questions.csv"):
    questions = []

    with open(path, "r", encoding="utf-8", newline="") as csvfile:        
        reader = csv.DictReader(csvfile)

        
        for row in reader:
            prompt = row["question"].strip()
            options = [row[f"option{i}"].strip() for i in (1, 2, 3)]
            answer = row["correct"].strip()

            questions.append({
                "prompt": prompt,
                "options": options,
                "answer": answer
                 })
    return questions


