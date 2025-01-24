TEMPLATE_FILE=periods.txt
PYTHON=python3  # Define the Python interpreter
MOVE_SCRIPT=src/read_image.py  # Path to your Python script
TEMPLATE_SCRIPT=src/create_template.py

init:
	@if [ -z "$(root_folder)" ]; then \
		echo "Usage: make init root_folder=<path_to_root_folder>"; \
		exit 1; \
	fi; \
	if [ -s $(root_folder)/$(TEMPLATE_FILE) ]; then \
		echo "Warning: A periods file already exists at $(root_folder)/$(TEMPLATE_FILE)."; \
		read -p "Do you want to reinitialize it? (yes/no) " choice; \
		if [ "$$choice" != "yes" ]; then \
			echo "Aborting initialization."; \
			exit 1; \
		fi; \
	fi; 
	$(PYTHON) $(TEMPLATE_SCRIPT) $(root_folder) $(TEMPLATE_FILE)

move:
	@if [ -z "$(root_folder)" ]; then \
		echo "Usage: make move root_folder=<path_to_root_folder> [period_file=<path_to_period_file>]"; \
		exit 1; \
	fi; \
	$(PYTHON) $(MOVE_SCRIPT) $(root_folder) $(period_file)
