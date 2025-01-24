TEMPLATE_FILE=periods.txt

init:
	@if [ -s $(TEMPLATE_FILE) ]; then \
		echo "Warning: A periods file already exists and is not empty."; \
		read -p "Do you want to reinitialize it? (yes/no) " choice; \
		if [ "$$choice" != "yes" ]; then \
			echo "Aborting initialization."; \
			exit 1; \
		fi; \
	fi; 
	@echo "# Time Periods Template" > $(TEMPLATE_FILE)
	@echo "# Enter periods of time in the format: YYYY-MM-DD to YYYY-MM-DD" >> $(TEMPLATE_FILE)
	@echo "# You can add a location after the dates if you want: Location" >> $(TEMPLATE_FILE)
	@echo "# Lines starting with # are ignored." >> $(TEMPLATE_FILE)
	@echo "" >> $(TEMPLATE_FILE)
	@echo "# Example:" >> $(TEMPLATE_FILE)
	@echo "# 2023-01-01 to 2023-01-15 = Barcelona" >> $(TEMPLATE_FILE)
	@echo "# 2023-06-01 to 2023-06-30" >> $(TEMPLATE_FILE)
	@echo "" >> $(TEMPLATE_FILE)
	@echo "# Enter your periods below:" >> $(TEMPLATE_FILE)
	@echo "Template created: $(TEMPLATE_FILE)"

