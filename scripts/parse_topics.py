import json
import re
import os

def parse_raw_text(file_path):
    """
    A foundational parser to read raw text dumps from College Board files
    and isolate individual questions based on standard numbering.
    """
    if not os.path.exists(file_path):
        print(f"Error: File {file_path} not found.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Regex to split by question numbers (e.g., "1. ", "2. ", "14. ")
    # This captures the number and splits the text nicely.
    raw_questions = re.split(r'\n(?=\d+\.\s)', content)
    
    parsed_questions = []
    
    for raw_q in raw_questions:
        if not raw_q.strip():
            continue
            
        # Clean up spacing
        cleaned_text = raw_q.strip()
        
        # Build a temporary structure
        question_data = {
            "raw_text": cleaned_text,
            "archetype_id": "type_1", # Defaulting to type_1 (text), to be refined manually or by AI
            "assigned_tags": {
                "big_idea": "Pending",
                "learning_objective": "Pending"
            },
            "mapped_data": {
                "stem": "",
                "options": {"A": "", "B": "", "C": "", "D": ""},
                "correct_answer": ""
            }
        }
        parsed_questions.append(question_data)
        
    return parsed_questions

if __name__ == "__main__":
    # Test path - adjust this to where your text files live
    target_file = "raw_data/topics1_2_1A.txt"
    print(f"Initializing parsing engine for: {target_file}")
    
    questions = parse_raw_text(target_file)
    print(f"Successfully isolated {len(questions)} potential question blocks.")
