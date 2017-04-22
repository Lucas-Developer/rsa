CC:="gcc"
FLAGS="-g"
.PHONY: paper

clear:
	rm -rf *.o
paper:
	cd paper ; \
	pdflatex sbc-template.tex ; \
	mv sbc-template.pdf  ../paper.pdf


test: clear
	${CC} ${FLAGS} -c **/*[^test].c
	${CC} ${FLAGS}  *.o rsa/rsa_test.c -lm -o test
	./test


