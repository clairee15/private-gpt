import subprocess

def list_files_in_container(container_name, directory):
    command = f"docker exec {container_name} ls {directory}"
    result = subprocess.run(command, shell=True, capture_output=True, text=True)
    if result.returncode == 0:
        print(f"Files in {directory}:")
        print(result.stdout)
    else:
        print("Failed to list files or directory not found.")
        print(result.stderr)

# Example usage:
container_name = "private-gpt-git"
directory = "/home/worker/app/.venv/lib/python3.11/site-packages/llama_index/llms/llama_cpp/"
list_files_in_container(container_name, directory)
