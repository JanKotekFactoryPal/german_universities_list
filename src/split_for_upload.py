def split_markdown_file(input_file, max_chars=25000):
    with open(input_file, 'r', encoding='utf-8') as file:
        content = file.read()

    sections = content.split('\n# ')
    sections = ['# ' + section if i != 0 else section for i, section in enumerate(sections)]

    split_files = []
    current_split = []
    current_length = 0

    for section in sections:
        section_length = len(section)
        if current_length + section_length > max_chars:
            split_files.append(current_split)
            current_split = [section]
            current_length = section_length
        else:
            current_split.append(section)
            current_length += section_length

    if current_split:
        split_files.append(current_split)

    for i, split in enumerate(split_files):
        output_file = f'split_{i + 1}.md'
        with open(output_file, 'w', encoding='utf-8') as file:
            file.write('\n'.join(split))
        print(f'Created {output_file} with {len("".join(split))} characters.')


input_file = 'universities_final_sorted.md'
split_markdown_file(input_file)
