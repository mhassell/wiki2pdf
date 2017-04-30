import wikipedia
import pdfkit
import os
from gtts import gTTS

class Page:

	def __init__(self):
		"""Set default pdfkit options."""
		self.pdf_options = {
    		'page-size': 'Letter',
    		'margin-top': '0.75in',
    		'margin-right': '0.75in',
    		'margin-bottom': '0.75in',
    		'margin-left': '0.75in',
    		'javascript-delay' : 2000,
    		'minimum-font-size': 512
		}

		self.target_dir = os.path.dirname(os.path.realpath(__file__))
		self.include_links = False

	def getArticle(self, article_title):
		"""Fetch the article from wiki by title."""
		self.page = wikipedia.page(article_title)
		try:
			print self.page.summary
		except wikipedia.exceptions.DisambiguationError as e:
			print "Multiple articles with that name: " + e.options

	def setURL(self,URL):
		"""Fetch the article by URL (not yet supported by the wikipedia module)"""
		pass

	def download(self):
		"""Download the article (and maybe the articles it links to."""

		links = [self.page, self.page.links] if self.include_links else [self.page]
		for link in links:
			linked_page = wikipedia.page(link)
			print "Downloading " + linked_page.url
			filename = self.target_dir + "/" + linked_page.title + '.pdf'
			pdfkit.from_url(linked_page.url, filename, options=self.pdf_options)

	def saveAudio(self):
		""" """
		links = [self.page, self.page.links] if self.include_links else [self.page]
		for link in links:
			linked_page = wikipedia.page(link)
			print "Downloading as audio: " + linked_page.url
			tts = gTTS(linked_page.content, lang='en')
			filename = self.target_dir + "/" + linked_page.title + '.mp3'
			tts.save(filename)
			

