proj: 	$(PLATFORM_CONFIG_FILE) $(PROJ_NAME).js

$(PROJ_NAME).js: $(OBJS)
	@echo $($(quiet_)link)
	@$(call link)
