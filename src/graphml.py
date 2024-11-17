import yaml
import pyyed

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

    for uni_type, universities in data['Universities_in_Berlin'].items():
        for university in universities:
            uni_name = university['Name']
            uni_node_id = uni_name.replace(" ", "_")
            create_node(graph, uni_node_id, uni_name, "rectangle", "#FFCC00")

            for faculty in university['Faculties']:
                faculty_name = faculty['Faculty']
                faculty_node_id = f"{uni_node_id}_{faculty_name.replace(' ', '_')}"
                create_node(graph, faculty_node_id, faculty_name, "ellipse", "#99CCFF")

                # Create edges between university and faculty
                graph.add_edge(uni_node_id, faculty_node_id)

                # Create edges between faculty's subject and Enumerations.Subjects
                subject_node_id = f"Subject_{faculty['Subject'].replace(' ', '_')}"
                create_node(graph, subject_node_id, faculty['Subject'], "ellipse", "#FF9999")
                graph.add_edge(faculty_node_id, subject_node_id)
                graph.add_edge(subject_node_id, "Enumerations_Subjects")

                # Create edges between faculty's city and Enumerations.Cities
                city_node_id = f"City_{faculty['City'].replace(' ', '_')}"
                create_node(graph, city_node_id, faculty['City'], "ellipse", "#99FF99")
                graph.add_edge(faculty_node_id, city_node_id)
                graph.add_edge(city_node_id, "Enumerations_Cities")

    return graph

def main():
    yaml_file_path = 'universities.yml'
    data = load_yaml(yaml_file_path)
    graph = generate_graphml(data)
    graph.write_graph('universities.graphml')

if __name__ == "__main__":
    main()