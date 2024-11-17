import re

def extract_faculties(markdown_content):
    faculties = []
    pattern = re.compile(r'(# .+?)(?=\n# |\Z)', re.DOTALL)
    matches = pattern.findall(markdown_content)
    for match in matches:
        copilot_score = int(re.search(r'\*\*Matching Score - Copilot:\*\* (\d+)', match).group(1))
        chatgpt_score = int(re.search(r'\*\*Matching Score - ChatGPT:\*\* (\d+)', match).group(1))
        faculties.append((copilot_score, chatgpt_score, match))
    return faculties

def sort_faculties(faculties):
    return sorted(faculties, key=lambda x: (x[0], x[1]), reverse=True)

def generate_sorted_markdown(faculties):
    sorted_markdown = ""
    for _, _, faculty in faculties:
        sorted_markdown += faculty + "\n\n"
    return sorted_markdown

if __name__ == "__main__":
    with open('universities_final.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    faculties = extract_faculties(markdown_content)
    sorted_faculties = sort_faculties(faculties)
    sorted_markdown_content = generate_sorted_markdown(sorted_faculties)

    with open('universities_final_sorted.md', 'w', encoding='utf-8') as file:
        file.write(sorted_markdown_content)