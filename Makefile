all:
	pdflatex template
	pdflatex template
	bibtex template
	pdflatex template


clean:
	rm *aux *bbl *blg *brf *lbl *log *pdf
