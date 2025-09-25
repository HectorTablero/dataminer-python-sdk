import os


def count_python_files(root_folder: str):
    total_files = 0
    total_lines = 0
    total_chars = 0

    for dirpath, _, filenames in os.walk(root_folder):
        for filename in filenames:
            if filename.endswith(".py"):
                total_files += 1
                file_path = os.path.join(dirpath, filename)
                try:
                    with open(file_path, "r", encoding="utf-8", errors="ignore") as f:
                        content = f.read()
                        total_lines += content.count("\n") + 1  # count lines
                        total_chars += len(content)
                except Exception as e:
                    print(f"Could not read {file_path}: {e}")

    return total_files, total_lines, total_chars


if __name__ == "__main__":
    folder = "../src/dataminer_sdk"
    files, lines, chars = count_python_files(folder)
    print(f"Python files: {files}")
    print(f"Total lines : {lines}")
    print(f"Total chars : {chars}")
