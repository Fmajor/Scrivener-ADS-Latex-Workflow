Scrivener-ADS-Latex-Workflow
============================

This is a workfolw using Scrivener_ + Zotero_ + Highlights_ + Latex_ to

1. Collect, manage papers (with their pdfs) and their reference (using Scrivener_ and Zotero_)
2. Easily highlight keywords and key Content using different colors, extract them into RTF (Rich Text Format) (using Highlights_)
3. Writing papers using MultiMarkdown_, compile it into latex file (using Scrivener_ and make)

.. _Scrivener: http://www.literatureandlatte.com/scrivener.php
.. _Zotero: https://www.zotero.org/
.. _Highlights: https://itunes.apple.com/cn/app/highlights-export-pdf-notes/id794854093
.. _Latex: https://www.latex-project.org/

Why
=====

Use MultiMarkdown_ Syntax in Scrivener_ to write latex?
-------------------------------------------------------

* MultiMarkdown_ syntax support many latex features
    examples:
    * citation and cross ref
      * "[#citekey]" will be compiled to \\citep{citekey}
      * "[#citekey;]" will be compiled to \\citet{citekey}
      * "[](#sec:1)" will be compiled to \\autoref{sec:1}
      * you can add refkey for sections, figures and equations
    * ordered and unordered lists
      * you can use the markdown "List" syntax,
        which will be compiled to `\begin{itemize} ... \begin{itemize}` or
        `\begin{enumerate} ... \end{enumerate}`
    * equations
      * you can use $...$ and $$....$$ command to insert inline and normal euqations
    * figures
      * you can use
      ::

        ![caption][label]
         [label]: $PATH width="0.30\textwidth" height="0.25\textheight"
      to insert figure (with label and simple options)
    * for other unsupported latex features,
      you can use latex code inside <!-- --> comment pair to archieve it.
    * the MultiMarkdown syntax make the source code more readable than raw latex code,
      but when you have to insert latex command, you need to put them in the
      comment pair (i use << >> pair in the project), this may make the code less
      readable. Don't mind, because
    * the most important: you can use Scrivener_ to manage your source code,
      so you no longer deal with long latex source code, you can efficiently
      organize them into hierarchical structure and get focused on the content
      itself when you are writing.
* Reasons i choose Scrivener_:
  * Scrivener is a powerful content-generation tool for writers that
    allows you to concentrate on composing and structuring long and
    difficult documents.
  * features: |2017-11-02T20-16-34|
  * suppport MultiMarkdown_ syntax and compile it into latex
  * **Tree structure to organize article content**:
    As you can see in the left Binder, the title in sections and subsections
    will be automatically compiled as "\\section{title}" or "\\subsection{title}",
    the sections 1 will have a label "sec:intro"
  * **History nagivation**: see the "<" and ">" button in the top left of the editor?
    when you move around in the Binder, your view history will be record and you can
    go around it.
  * **The scrivening feature**: now i use cmd+click to select 4 text in the binder,
    they are collected together in the text editor!! This is the most remarkable feature
    and also where the name of this software come from.
  * **Rich text**: the format of all the texts are RTF (Rich Text Format), you can color
    all the text, inserting images every where.
  * **Reference list**: the reference list are shown at the bottom right, you can goto this
    references by a simple click, also notice the three blue word "Zheng.etal2011",
    "Zheng.etal2011" and "JeesonDaniel2012", they are references links, and are clickable
  * |2017-11-02T20-31-56|
  * using python script, i can import paper info from Zotero_ into Scrivener_:
    here is an example,
    * papers are listed in inverse time order in the Binder.
    * Basic information are collected as the main text.
    * the cross reference relation are show in their Reference list
    * you can access the pdf directly in the Reference list
  * other useful features: keyworkds, metadata, snapshorts, collections...
  * you need some time to learn all the Scrivener features, but after
    that, you will find it very helpful when you collect, extract and refine
    informations from numerous resources.
* Reasons i choose Highlights_ to read paper:
  * |2017-11-02T20-46-50|
  * as shown in the figure, it has the simplest way to highlight, comment
    pdf with multipile color, among all PDF readers i have ever used.
  * |2017-11-02T20-49-08|
  * it can collect all the highlight text and the comments text in markdown format
  * |2017-11-02T20-58-22|
  * another script can extract all the text into RTF format, and you can put them
    into your scrivener project!

.. |2017-11-02T20-16-34| figure:: asset/2017-11-02T20-16-34.png
	 :alt: 2017-11-02T20-16-34
.. |2017-11-02T20-31-56| figure:: asset/2017-11-02T20-31-56.png
	 :alt: 2017-11-02T20-31-56
.. |2017-11-02T20-46-50| figure:: asset/2017-11-02T20-46-50.png
	 :alt: 2017-11-02T20-46-50
.. |2017-11-02T20-49-08| figure:: asset/2017-11-02T20-49-08.png
	 :alt: 2017-11-02T20-49-08
.. |2017-11-02T20-58-22| figure:: asset/2017-11-02T20-58-22.png
	 :alt: 2017-11-02T20-58-22
.. _MultiMarkdown: http://fletcherpenney.net/multimarkdown/

Requirements and Configs
========================

0. macOS with python3 and make
1. Scrivener_
2. Zotero_
   Install the BetterBibtex_ Plugin, then in Preferences ==> Better BibTeX
   1. in Citation keys, set Citation key format to [auth.etal][year] and check "Force citation key to ASCII"
   2. in Export, check "Export BibteX as ASCII"
3. Latex_
   Install latex and make sure you have the latex commands in Shell
4. Highlights_  (optional)
   Preferences ==> Customize ==> Annotation header ==> ONLY check Color category

.. _BetterBibtex: https://github.com/retorquere/zotero-better-bibtex

Usage
=======

* clone this repository

import collections in Zotero into Scrivener
-------------------------------------------
* export Zotero collections:
    1. make new collections (LAE in the following example) and collect papers
       the papers should come from ADS_ or arxiv_
    2. export collections into the "references" folder using these two format,
       Better Bibtex (.bib file) and BetterBibTex JSON(.json file),
       into the references folder.
       The .bib file is used by latex and the .json file is used by scripts
* use scripts to generate paper database and import them into Scrivener (make sure you have .json files in the reference folder)
  1. **make query** will generate the database and query all the papers in ADS and generate Cross reference relation between them, this will take some time
  2. **make offline** will only generate the database
  3. after **make query** or **make offline**, your can **make gen** to import the papers into Scirvener

.. _ADS: https://ui.adsabs.harvard.edu/
.. _arxiv: http://arxiv.org/

Using MultiMarkdown to write paper, compile them into latex file and pdfs
-------------------------------------------------------------------------

we have two AASTeX_ based template and convert them into MultiMarkdown_ format in the Main.scriv project,
all the useful syntax are included in the SimpleOneColumn and AASTeX6.1 demo, you should read the "README"
Text in the Draft folder and inside each demo, then follow them to compiled these two demos,
after that, you can duplicate one of these demos or convert your own Latex template into MultiMarkdown_ version.

A makefile to help compile latex file
---------------------------------------

when you follow the tutorial in the Main.scriv and get the compiled latex file
``<$compileGroup>.tex/<$compileGroup>.tex``
you can use ``make tex`` to copy one makefile and one script into all the ``*.tex`` folder

then cd into the *.tex folder and type ``make``, you will get the final pdf

Also, you can choose to use your own IDE to compile the tex file.

.. _AASTeX: http://journals.aas.org/authors/aastex.html#_download
