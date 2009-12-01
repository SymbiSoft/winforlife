import appuifw
import globalui
import re
import urllib
import e32
import time

__title__ = "WinForLife"
__version__ = "0.1"
__shell__ = 1

class _WinForLife:
	def __init__(self):
		self.lock = e32.Ao_lock()
		appuifw.app.title = unicode("%s %s" % (__title__, __version__))
		appuifw.app.exit_key_handler = self.exit_key_handler
		appuifw.app.menu = [(u"Verifica Schedina", self.get), (u"Ultima Estrazione", self.lastget), (u"Info", self.info), (u"Esci", self.exit_key_handler)]
		self.txt = appuifw.Text()
		appuifw.app.body = self.txt

	def exit_key_handler(self):
		self.lock.signal()
		if not __shell__:
			sys.exit()

	def run(self):
		self.info()
		self.lock.wait()

	def info(self):
		self.txt.set(u"Benvenuti in %s.\n\nQuesta semplice applicazione necessita di una connessione ad internet per poter verificare la vincita della propria schedina WinForLife.\n" % __title__)
		self.txt.add(u"Per avviare la verifica selezionare dal menu 'Verifica Schedina' ed inserire il numero della schedina appena chiesto. Subito dopo sara' necessario inserire anche il numero del concorso SENZA inserire anche i numeri seguiti dal segno /\n")
		self.txt.add(u"Grazie.")

	def lastget(self):
		URLdiverifica = u"http://www.sistemiwinforlife.com/"
		self.txt.set(u"Attendere ...\nVerifica in corso ...")
		paginaWEB = urllib.urlopen(URLdiverifica).read()
		try:
			concorso = (re.search('<span class="numConcorso">\x0d\x0a(.*?)</span>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			concorso = "Errore"
		try:
			giorno = (re.search('DEL\x20<span class="numConcorso">\x0d\x0a(.*?)</span>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			giorno = "Errore"
		try:
			ora = (re.search('ORE\x20<span class="numConcorso">\x0d\x0a(.*?)</span>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			ora = "Errore"
		try:
			primo = (re.search('<div class="numEstrazione" id="priEstr">\x0d\x0a(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			primo = "Errore"
		try:
			secondo = (re.search('<div class="numEstrazione" id="secEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			secondo = "Errore"
		try:
			terzo = (re.search('<div class="numEstrazione" id="terEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			terzo = "Errore"
		try:
			quarto = (re.search('<div class="numEstrazione" id="quaEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			quarto = "Errore"
		try:
			quinto = (re.search('<div class="numEstrazione" id="cinEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			quinto = "Errore"
		try:
			sesto = (re.search('<div class="numEstrazione" id="sesEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			sesto = "Errore"
		try:
			settimo = (re.search('<div class="numEstrazione" id="setEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			settimo = "Errore"
		try:
			ottavo = (re.search('<div class="numEstrazione" id="ottEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			ottavo = "Errore"
		try:
			nono = (re.search('<div class="numEstrazione" id="nonEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			nono = "Errore"
		try:
			decimo = (re.search('<div class="numEstrazione" id="decEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			decimo = "Errore"
		try:
			numerone = (re.search('<div class="numEstrazione" id="numEstr">\x0d\x0a\x20\x20(.*?)</div>', paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			numerone = "Errore"
		testo = "Concorso:\n%s del %s %s\nCombinazione:\n%s %s %s %s %s %s %s %s %s %s      %s" % (concorso, giorno, ora, primo, secondo, terzo, quarto, quinto, sesto, settimo, ottavo, nono, decimo, numerone)
		self.txt.set(unicode(testo))

	def get(self):
		codice = appuifw.query(u"Inserire il codice riportato sulla schedina", "text")
		if not codice:
			return
		giocata = appuifw.query(u"Inserire il numero del concorso", "number")
		if not giocata:
			return
		URLdiverifica = u"http://servizi.sisal.it/verificavincite/popup.jsp?cod=%s&conc=%s" % (codice, giocata)
		self.txt.set(u"Attendere ...\nVerifica in corso ...")
		try:
			paginaWEB = urllib.urlopen(URLdiverifica).read()
		except Exception, err:
			appuifw.note(unicode(err))
			return
		try:
			ricevitoria = (re.search("<font class=testo8>giocata presso la ricevitoria <b>(.*?)\x0d\x0a\t\t\t\t\t\t\t\t\t\t\t\t\t\t</font>", paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			ricevitoria = "Errore"
		try:
			concorso = (re.search("vincente relativa al concorso(.*?)\x0d\x0a\t\t\t\t\t\t\t\t\t\t\t\t\t</font></b>", paginaWEB).group(1))
			concorso = concorso.replace("\t", " ")
		except Exception, err:
			appuifw.note(unicode(err))
			concorso = "Errore"
		try:
			combinazione = (re.search("<font class=testo9b color=\"#00147D\"><b>(.*?)</b></font>", paginaWEB).group(1))
			combinazione = combinazione.replace("&nbsp;", " ")
		except Exception, err:
			appuifw.note(unicode(err))
			combinazione = "Errore"
		try:
			risultato = (re.search("<font class=tit5c>(.*?)</font>", paginaWEB).group(1))
		except Exception, err:
			appuifw.note(unicode(err))
			risultato = "Errore"
		
		testo = "Ricevitoria:\n%s\n\nConcorso:\n%s\n\nCombinazione:\n%s\n\nEsito:\n%s" % (ricevitoria, concorso, combinazione, risultato)
		self.txt.set(unicode(testo))

application = _WinForLife()
application.run()
