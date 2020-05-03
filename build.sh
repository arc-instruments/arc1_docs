#!/bin/bash

pandoc manual.txt --number-sections --template=template.html5 \
	--css=manual.css --pdf-engine=weasyprint -o arc1docs/manual.pdf
