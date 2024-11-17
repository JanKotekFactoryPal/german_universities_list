import pyyed
import yaml

def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)

def create_node(graph, node_id, label, shape, shape_fill):
    if node_id not in graph.existing_entities:
        graph.add_node(node_id, label=label, shape=shape, shape_fill=shape_fill)

def generate_graphml(data):
    graph = pyyed.Graph()

    # Create Enumerations nodes
    create_node(graph, "Enumerations_Subjects", "Enumerations.Subjects", "rectangle", "#FF9999")
    create_node(graph, "Enumerations_Cities", "Enumerations.Cities", "rectangle", "#FF9999")

    subjects = {}
    cities = {}

    # Load enumerations from YAML
    for subject in data['Enumerations']['Subjects']:
        subject_node_id = f"Subject_{subject.replace(' ', '_')}"
        create_node(graph, subject_node_id, subject, "ellipse", "#FF9999")
        graph.add_edge(subject_node_id, "Enumerations_Subjects")
        subjects[subject] = subject_node_id

    for city in data['Enumerations']['Cities']:
        city_node_id = f"City_{city.replace(' ', '_')}"
        create_node(graph, city_node_id, city, "ellipse", "#99FF99")
        graph.add_edge(city_node_id, "Enumerations_Cities")
        cities[city] = city_node_id

    for uni_type, universities in data['Universities_in_Berlin'].items():
        group = graph.add_group(uni_type.replace(" ", "_"), label=uni_type)
        for university in universities:
            uni_name = university['Name']
            uni_node_id = uni_name.replace(" ", "_")
            uni_group = graph.add_group(uni_node_id, label=uni_name)
            create_node(graph, uni_node_id, uni_name, "rectangle", "#FFCC00")

            for faculty in university['Faculties']:
                faculty_name = faculty['Faculty']
                faculty_node_id = f"{uni_node_id}_{faculty_name.replace(' ', '_')}"
                create_node(graph, faculty_node_id, faculty_name, "ellipse", "#99CCFF")

                # Create edges between university and faculty
                graph.add_edge(uni_node_id, faculty_node_id)

                # Create edges between faculty's subject and Enumerations.Subjects
                subject_node_id = subjects[faculty['Subject']]
                graph.add_edge(faculty_node_id, subject_node_id)

                # Create edges between faculty's city and Enumerations.Cities
                city_node_id = cities[faculty['City']]
                graph.add_edge(faculty_node_id, city_node_id)


    return graph

def main():
    yaml_file_path = 'universities.yml'
    data = load_yaml(yaml_file_path)
    graph = generate_graphml(data)
    graph.write_graph('universities.graphml')

if __name__ == "__main__":
    main()
