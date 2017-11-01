SHELL:=/bin/zsh
all:
	cat makefile
	@echo "you need to ./env first"
env:
	@echo "source setup.sh"
query:
	./paperSystem/paperSystemStep1
offline:
	./paperSystem/paperSystemStep1 --offline
gen:
	./paperSystem/paperSystemStep2
update:
	./paperSystem/paperSystemUpdate
2rtf:
	./paperSystem/2rtf
