.DEFAULT_GOAL := help


### QUICK
# ¯¯¯¯¯¯¯

install: server.install ## Install

stop: server.stop ## Stop


include makefiles/server.mk
include makefiles/test.mk
include makefiles/database.mk
include makefiles/client.mk
