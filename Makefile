all:
	pdflatex EGauthorGuidelines-eurovis18-full
	pdflatex EGauthorGuidelines-eurovis18-full
	bibtex EGauthorGuidelines-eurovis18-full
	pdflatex EGauthorGuidelines-eurovis18-full


clean:
	rm *aux *bbl *blg *brf *lbl *log *pdf
