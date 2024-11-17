import yaml

def generate_markdown(data):
    markdown = ""
    for university_type, universities in data.items():
        markdown += f"# {university_type.replace('_', ' ')}\n"
        for university, faculties in universities.items():
            markdown += f"## {university.replace('_', ' ')}\n"
            for faculty, details in faculties.items():
                markdown += f"### {faculty}\n"
                markdown += f"**City:** {details.get('City', 'N/A')}\n\n"
                markdown += f"**Description:** {details.get('Description', 'No description available.')}\n\n"
                markdown += f"**Subject:** {details.get('Subject', 'Unknown Subject')}\n\n"
                markdown += f"**Matching Reason:** {details.get('matching_reason', 'N/A')}\n\n"
                markdown += f"**Matching Score:** {details.get('matching_score', 'N/A')}\n\n"
    return markdown

if __name__ == "__main__":
    with open('universities.yml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        markdown_content = generate_markdown(data)
        with open('universities.md', 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)