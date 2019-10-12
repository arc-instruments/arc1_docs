## Documentation for ArC 1

This repository holds the documentation for ArC 1. It provides information on
setting up ArC 1 as well as using and updating the software interface.

Documentation is contained within `manual.txt` and is authored in pandoc
markdown flavour. In order to produce either the HTML or the PDF version pandoc
needs to be installed. For more details on how to install and use pandoc follow
the details on the [official website](https://pandoc.org/installing.html).
After installing pandoc it is straightforward to generate the HTML version of
the documentation by running

```
pandoc manual.txt --number-sections --template=template.html5
  --css=manual.css -o manual.html
```

To generate the PDF version of the manual you will need
[Weasyprint](https://weasyprint.org/) in addition to pandoc. If you have python
installed just run

```
pip install weasyprint
```

If you are on Windows you will need to have the GTK+ runtime installed. Follow
the details on the [Weasyprint
website](https://weasyprint.readthedocs.io/en/latest/install.html#windows) for
more details.

Now pandoc can generate a PDF version of the same HTML file by running

```
pandoc manual.txt --number-sections --template=template.html5
  --css=manual.css --pdf-engine=weasyprint -o manual.pdf
```

Just ensure that the `weasyprint` executable is in your path. A build script
(`build.bat` or `build.sh`) is provided for convenience.
