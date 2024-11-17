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
                    "description": details.get("Description", "No description available."),
                    "admission_criteria": details.get("admission_criteria", "N/A"),
                    "admission_ratio": details.get("admission_ratio", "N/A"),
                    "attendants": details.get("attendants", "N/A"),
                    "average_rating": details.get("average_rating", "N/A"),
                    "best_rating_comment": details.get("best_rating_comment", "N/A"),
                    "cooperating_companies": details.get("cooperating_companies", []),
                    "dual_ausbildung": details.get("dual_ausbildung", "N/A"),
                    "international_students_ratio": details.get("international_students_ratio", "N/A")
                })

    faculties_list.sort(key=lambda x: x["matching_score"], reverse=True)

    markdown = ""
    for faculty in faculties_list:
        markdown += f"# {faculty['name']}\n\n"
        markdown += f"> **Matching Score:** {faculty['matching_score']} \>\n"
        markdown += f"> **Matching Reason:** {faculty['matching_reason']}\n\n"
        markdown += f"- **University Type:** {faculty['university_type']}\n"
        markdown += f"- **Description:** {faculty['description']}\n"
        markdown += f"- **Subject:** {faculty['subject']}\n"
        markdown += f"- **City:** {faculty['city']}\n\n"
        markdown += f"- **Admission Criteria:** {faculty['admission_criteria']}\n"
        markdown += f"- **Admission Ratio:** {faculty['admission_ratio']}\n"
        markdown += f"- **Attendants:** {faculty['attendants']}\n"
        markdown += f"- **Average Rating:** {faculty['average_rating']}\n"
        markdown += f"- **Best Rating Comment:** {faculty['best_rating_comment']}\n"
        markdown += f"- **Cooperating Companies:** {', '.join(faculty['cooperating_companies'])}\n"
        markdown += f"- **Dual Ausbildung:** {faculty['dual_ausbildung']}\n"
        markdown += f"- **International Students Ratio:** {faculty['international_students_ratio']}\n\n"
        markdown += "* * *\n\n"

    return markdown

if __name__ == "__main__":
    with open('universities.yml', 'r', encoding='utf-8') as file:
        data = yaml.safe_load(file)
        markdown_content = generate_markdown(data)
        with open('universities.md', 'w', encoding='utf-8') as md_file:
            md_file.write(markdown_content)