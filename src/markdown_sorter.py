import re

def merge_scores_and_reasons(markdown_content):
    pattern = re.compile(r'> \*\*Matching Score - (ChatGPT|Copilot):\*\* (\d+)\n> \*\*Matching Reason - \1:\*\* (.+)')
    merged_content = pattern.sub(r'> [Matching Score - \1]: \2 Matching Reason - \1: \3', markdown_content)
    return merged_content

if __name__ == "__main__":
    with open('universities_final_sorted.md', 'r', encoding='utf-8') as file:
        markdown_content = file.read()

    merged_markdown_content = merge_scores_and_reasons(markdown_content)

    with open('universities_final_sorted2.md', 'w', encoding='utf-8') as file:
        file.write(merged_markdown_content)