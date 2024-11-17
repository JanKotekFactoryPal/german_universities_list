import yaml

def generate_markdown(data):
    faculties_list = []
    for university_type, universities in data.items():
        for university, faculties in universities.items():
            for faculty, details in faculties.items():
                faculties_list.append({
                    "name": f"{university.replace('_', ' ')} / {faculty}",
                    "matching_score": details.get("matching_score", "N/A"),
                    "matching_reason": details.get("matching_reason", "N/A"),
                    "university_type": university_type.replace('_', ' '),
                    "subject": details.get("Subject", "Unknown Subject"),
                    "city": details.get("City", "N/A"),
                    "description": details.get("Description", "No description available.")
                })

    faculties_list.sort(key=lambda x: x["matching_score"], reverse=True)

    markdown = ""
    for faculty in faculties_list:
        markdown += f"# {faculty['name']}\n\n"
        markdown += f"> **Matching Score:** {faculty['matching_score']} \n>\n"
        markdown += f"> **Matching Reason:** {faculty['matching_reason']}\n\n"
        markdown += f"- **University Type:** {faculty['university_type']}\n"
        markdown += f"- **Description:** {faculty['description']}\n"
        markdown += f"- **Subject:** {faculty['subject']}\n"
        markdown += f"- **City:** {faculty['city']}\n\n"
        markdown += "* * *\n\n"

    return markdown

if __name__ == "__main__":
    with open('universities.yml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        markdown_content = generate_markdown(data)
        with open('universities.md', 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)