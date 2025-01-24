import os

def create_template_file(root_folder:str, template_file:str):
    template_content = (
        "# Time Periods Template\n"
        "# Enter periods of time in the format: YYYY-MM-DD to YYYY-MM-DD\n"
        "# You can add a location after the dates if you want: Location\n"
        "# Lines starting with # are ignored.\n"
        "\n"
        "# Example:\n"
        "# 2023-01-01 to 2023-01-15 = Barcelona\n"
        "# 2023-06-01 to 2023-06-30\n"
        "\n"
        "# Enter your periods below:\n"
    )
    
    os.makedirs(root_folder, exist_ok=True)
    file_path = os.path.join(root_folder, template_file)
    
    with open(file_path, "w") as f:
        f.write(template_content)
    
    print(f"Template created: {file_path}")


if __name__ == "__main__":
    import sys

    DEFAULT_PERIOD_FILE_NAME='periods.txt'
    root_folder = sys.argv[1]
    periods_file_name = sys.argv[2] if len(sys.argv) >= 3 else DEFAULT_PERIOD_FILE_NAME

    create_template_file(root_folder=root_folder, template_file=periods_file_name)