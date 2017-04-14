import wikipedia
import pdfkit
import os

class Page:

	def __init__(self):
		"""Set default pdfkit options"""
		self.pdfOptions = {
    		'page-size': 'Letter',
    		'margin-top': '0.75in',
    		'margin-right': '0.75in',
    		'margin-bottom': '0.75in',
    		'margin-left': '0.75in',
    		'javascript-delay' : 2000,
    		'minimum-font-size': 512
		}

		self.targetDir = os.getcwd() #os.path.dirname(os.path.realpath(__file__))
		self.includeLinks = False

	def getArticle(self, articleTitle):
		"""fetch the article from wiki by title"""
		self.page = wikipedia.page(articleTitle)
		try:
			self.page.summary
		except wikipedia.exceptions.DisambiguationError as e:
			print "Multiple articles with that name: " + e.options

	def setURL(self,URL):
		"""fetch the article by URL"""
		pass

	def download(self):
		"""download the article (and maybe the articles it links to"""
		if self.includeLinks == False:
			filename = self.targetDir+"/"+self.page.title+'.pdf'
			pdfkit.from_url(self.page.url, filename, options = self.pdfOptions)
		else:
			for link in self.page.links:
				linkedPage = wikipedia.page(link)
				print "Downloading " + linkedPage.url
				filename = self.targetDir+"/"+linkedPage.title+'.pdf'
				pdfkit.from_url(linkedPage.url, filename, options=self.pdfOptions)

