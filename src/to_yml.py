import yaml
import re

def parse_markdown(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    faculties = {}
    faculty_pattern = re.compile(r'# (.+?) / (.+?)\n\n> \*\*Matching Score:\*\* (\d+)\s*\n> \*\*Matching Reason:\*\* (.+?)\n\n- \*\*University Type:\*\* (.+?)\n- \*\*Description:\*\* (.+?)\n- \*\*Subject:\*\* (.+?)\n- \*\*City:\*\* (.+?)\n- \*\*Admission Criteria:\*\* (.+?)\n- \*\*Admission Ratio:\*\* (.+?)\n- \*\*Attendants:\*\* (.+?)\n- \*\*Average Rating:\*\* (.+?)\n- \*\*Best Rating Comment:\*\* (.+?)\n- \*\*Cooperating Companies:\*\* (.*?)\n- \*\*Dual Ausbildung:\*\* (.+?)\n- \*\*International Students Ratio:\*\* (.+?)\n- \*\*Study Abroad Opportunities:\*\* (.+?)\n- \*\*Language of Instruction:\*\* (.+?)\n- \*\*Global Ranking:\*\* (.+?)\n- \*\*Faculty Webpage:\*\* \[(.+?)\]\((.+?)\)\n\n\*\*Study Programs:\*\*\n\n((?:- \*\*.+?\*\*: .+?\n)+)\n\*\*\*', re.DOTALL)

    for match in faculty_pattern.finditer(content):
        university_name, faculty_name, matching_score, matching_reason, university_type, description, subject, city, admission_criteria, admission_ratio, attendants, average_rating, best_rating_comment, cooperating_companies, dual_ausbildung, international_students_ratio, study_abroad_opportunities, language_of_instruction, global_ranking, faculty_webpage, faculty_webpage_url, study_programs = match.groups()

        if university_name not in faculties:
            faculties[university_name] = {}

        faculties[university_name][faculty_name] = {
            'matching_score': int(matching_score),
            'matching_reason': matching_reason,
            'university_type': university_type,
            'description': description,
            'subject': subject,
            'city': city,
            'admission_criteria': admission_criteria,
            'admission_ratio': admission_ratio,
            'attendants': attendants,
            'average_rating': average_rating,
            'best_rating_comment': best_rating_comment,
            'cooperating_companies': cooperating_companies,
            'dual_ausbildung': dual_ausbildung,
            'international_students_ratio': international_students_ratio,
            'study_abroad_opportunities': study_abroad_opportunities,
            'language_of_instruction': language_of_instruction,
            'global_ranking': global_ranking,
            'faculty_webpage': faculty_webpage_url,
            'study_programs': parse_study_programs(study_programs)
        }

    return faculties

def parse_study_programs(study_programs_text):
    study_programs = {}
    program_pattern = re.compile(r'- \*\*(.+?)\*\*: (.+?)\n')
    for match in program_pattern.finditer(study_programs_text):
        program_name, program_description = match.groups()
        study_programs[program_name] = program_description
    return study_programs

def write_yaml(data, output_path):
    with open(output_path, 'w', encoding='utf-8') as file:
        yaml.dump(data, file, allow_unicode=True, default_flow_style=False)

if __name__ == "__main__":
    markdown_file_path = 'universities_final_sorted.md'
    yaml_file_path = 'universities.yml'
    universities_data = parse_markdown(markdown_file_path)
    write_yaml(universities_data, yaml_file_path)