SHELL:=/bin/bash
all:
	cat makefile
	@echo "you need to ./env first"
query:
	./bin/paperSystemStep1
offline:
	./bin/paperSystemStep1 --offline
gen:
	./bin/paperSystemStep2
update:
	./bin/paperSystemUpdate
2rtf:
	./bin/2rtf
tex:
	@./bin/copyMakefiles2Tex
	@echo "copy makefile and compile script to all *.tex folder"
