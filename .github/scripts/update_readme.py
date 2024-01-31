import os
import yaml


def find_docker_compose_files():
    files = []
    for root, dirs, files_in_dir in os.walk('.'):
        for file in files_in_dir:
            if file.startswith('docker-compose') and file.endswith('.yml'):
                files.append(os.path.join(root, file))
    return files


def extract_service_names(file_path):
    with open(file_path, 'r') as file:
        compose_dict = yaml.safe_load(file)
    return list(compose_dict.get('services', {}).keys())


def update_readme(services):
    readme_path = 'README.md'
    with open(readme_path, 'r') as file:
        lines = file.readlines()

    start_index = -1
    end_index = -1
    for i, line in enumerate(lines):
        if line.startswith('## Services'):
            start_index = i + 2
        elif start_index != -1 and line.startswith('## '):
            end_index = i
            break

    if start_index == -1 or end_index == -1:
        print("Couldn't find the correct place to update in README.md")
        return

    new_content = []
    for service, path in services.items():
        new_content.append(f"- **{service.title()}**: Configured in `{path}`\n")

    lines[start_index:end_index] = new_content

    with open(readme_path, 'w') as file:
        file.writelines(lines)


def main():
    docker_files = find_docker_compose_files()
    services = {}
    for file_path in docker_files:
        for service in extract_service_names(file_path):
            services[service] = os.path.relpath(file_path).replace('\\', '/')

    update_readme(sorted(services))


if __name__ == "__main__":
    main()
