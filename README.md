A tool for downloading wiki articles to PDF to enjoy on long flights, when your iPad doesn't have data, or you are over your data limit (grumbles).

Use:

	import wiki2pdf

	page=wiki2pdf.Page()
	
	page.getArticle('Georg Cantor')

	page.download()	# saves the article as PDF to the directory the script is in

	# set this first to another directory if you want to save the pdf there
	page.target_dir = '/Desktop'

	# want to save all the pages the article links to?
	page.include_links = True

	page.saveAudio()
	
		
	
TBD:

1. (done) download a wiki article to pdf

2. (done) include the option to download articles it links to

3. text to speech (need to parse just the article, and not the TeX code, index, links, and extra info)

4. (done but super slow) export article as mp3 for an audiobook experience!

5. Access a wiki article by URL (doesn't seem to be an option with this library)

6. Better error handling (ambiguous pages, for example) 
