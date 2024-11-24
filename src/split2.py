import os
import yaml

# Load the YAML file
with open('ranked_universities_o1.yaml', 'r') as file:
    data = yaml.safe_load(file)

# Ensure the output directory exists
output_dir = 'faculties'
os.makedirs(output_dir, exist_ok=True)

# Process each faculty
for faculty, details in data.items():
    # Extract university name and faculty name
    university_name, faculty_name = faculty.split(' / ')

    # Extract matching score
    matching_score = details.get('matching_score', '0')

    # Create a valid filename
    filename = f"{matching_score}{university_name.replace(' ', '_')}{faculty_name.replace(' ', '_')}.yaml"
    filepath = os.path.join(output_dir, filename)

    # Write the faculty details to a new YAML file
    with open(filepath, 'w') as outfile:
        yaml.dump({faculty: details}, outfile, default_flow_style=False)

print("Files have been successfully created in the 'faculties' directory.")