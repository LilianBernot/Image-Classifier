TEMPLATE_FILE=periods.txt
PYTHON=python3  # Define the Python interpreter
SCRIPT=src/read_image.py  # Path to your Python script

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
	@echo "# Time Periods Template" > $(root_folder)/$(TEMPLATE_FILE)
	@echo "# Enter periods of time in the format: YYYY-MM-DD to YYYY-MM-DD" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "# You can add a location after the dates if you want: Location" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "# Lines starting with # are ignored." >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "# Example:" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "# 2023-01-01 to 2023-01-15 = Barcelona" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "# 2023-06-01 to 2023-06-30" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "# Enter your periods below:" >> $(root_folder)/$(TEMPLATE_FILE)
	@echo "Template created: $(root_folder)/$(TEMPLATE_FILE)"

move:
	@if [ -z "$(root_folder)" ]; then \
		echo "Usage: make move root_folder=<path_to_root_folder> [period_file=<path_to_period_file>]"; \
		exit 1; \
	fi; \
	$(PYTHON) $(SCRIPT) $(root_folder) $(period_file)
