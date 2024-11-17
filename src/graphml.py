import pyyed
import yaml


def load_yaml(file_path):
    with open(file_path, 'r') as file:
        return yaml.safe_load(file)


def create_node(graph, node_id, label, shape, color):
    graph.add_node(node_id, label=label, shape=shape, fill=color)


def generate_graphml(data):
    graph = pyyed.Graph()

    for uni_type, universities in data['Universities_in_Berlin'].items():
        for university in universities:
            uni_name = university['Name']
            uni_node_id = uni_name.replace(" ", "_")
            create_node(graph, uni_node_id, uni_name, "rectangle", "#FFCC00")

            for faculty in university['Faculties']:
                faculty_name = faculty['Faculty']
                faculty_node_id = f"{uni_node_id}_{faculty_name.replace(' ', '_')}"
                create_node(graph, faculty_node_id, faculty_name, "ellipse", "#99CCFF")

                graph.add_edge(uni_node_id, faculty_node_id)

    return graph


def main():
    yaml_file_path = 'universities.yml'
    data = load_yaml(yaml_file_path)
    graph = generate_graphml(data)
    graph.write_graph('universities.graphml')


if __name__ == "__main__":
    main()
