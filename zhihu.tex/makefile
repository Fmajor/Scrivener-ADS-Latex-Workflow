SHELL = /bin/bash
compileGroup := zhihu
all:
	echo "make all"
	./compileTex

draft:
	echo "set current version as draft"
	cp $(compileGroup).tex draft.tex

milestone:
	echo "set current version as milestone"
	cp $(compileGroup).tex milestone.tex

diffmilestone:
	$(eval toDiff = milestone)
	latexpand $(compileGroup).tex --keep-comments --fatal -o $(compileGroup)-flatten.tex
	latexpand ${toDiff}.tex --keep-comments --fatal -o ${toDiff}-flatten.tex
	latexdiff ${toDiff}-flatten.tex $(compileGroup)-flatten.tex --preamble=../configs/blank.tex  > diff.tex
	$(eval file=diff)
	#@echo ${file}
	pdflatex ${file} && bibtex ${file} && pdflatex ${file} && pdflatex ${file}
	open ${file}.pdf

difflast:
	$(eval toDiff = last)
	latexpand $(compileGroup).tex --keep-comments --fatal -o $(compileGroup)-flatten.tex
	latexpand ${toDiff}.tex --keep-comments --fatal -o ${toDiff}-flatten.tex
	latexdiff ${toDiff}-flatten.tex $(compileGroup)-flatten.tex --preamble=../configs/blank.tex  > diff.tex
	$(eval file=diff)
	#@echo ${file}
	pdflatex ${file} && bibtex ${file} && pdflatex ${file} && pdflatex ${file}
	open ${file}.pdf

diffdraft:
	$(eval toDiff = draft)
	latexpand $(compileGroup).tex --keep-comments --fatal -o $(compileGroup)-flatten.tex
	latexpand ${toDiff}.tex --keep-comments --fatal -o ${toDiff}-flatten.tex
	latexdiff ${toDiff}-flatten.tex $(compileGroup)-flatten.tex --preamble=../configs/blank.tex  > diff.tex
	$(eval file=diff)
	#@echo ${file}
	pdflatex ${file} && bibtex ${file} && pdflatex ${file} && pdflatex ${file}
	open ${file}.pdf

.PHONY: clean
clean:
	rm *.aux 2>/dev/null || echo
	rm *.log 2>/dev/null || echo
	rm *.toc 2>/dev/null || echo
	rm *.bbl 2>/dev/null || echo
	rm *.blg 2>/dev/null || echo
	rm *.out 2>/dev/null || echo
	rm *.flt 2>/dev/null || echo
	rm *.synctex.gz 2>/dev/null || echo
