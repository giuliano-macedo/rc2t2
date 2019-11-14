from flask import Flask,redirect,send_from_directory,request
import markdown2
import pickle
import re
def safe(str):
	regex=re.compile(r"[A-Za-zÀ-ÖØ-öø-ÿ0-9#*\n\ ]")
	ans="".join((c for c in str if regex.match(c)))
	return markdown2.markdown(ans)
class Comment:
	def __init__(self,nome,comentario):
		self.nome=nome
		self.comentario=comentario
	def to_html(self):
		nome=self.nome
		comentario=self.comentario

		return f"<div class='comment'><b>{nome}</b> disse: <br> <br>{comentario}</div>"
		# return f"<div class='comment'><b>{safe(nome)}</b> disse :<br>{safe(comentario)}</div>"

class CommentDAO:
	def __init__(self):
		self.list=[]
		try:
			self.list=pickle.load(open("comments.p","rb"))
		except Exception:
			pass
	def add(self,nome,comentario):
		self.list.append(Comment(nome,comentario))
		pickle.dump(self.list,open("comments.p","wb"))
	def __iter__(self):
		return iter(self.list)

dao=CommentDAO()
app=Flask(__name__)

@app.route("/")
def root():
	return redirect("index.html")
@app.route('/<path:path>')
def public_html(path):
	return send_from_directory("public_html",path)
@app.route("/index.html")
def index():
	body_text=open("lorem.txt").read()
	comments="<br>".join((comment.to_html() for comment in dao))
	return open("forum.html").read().format(**locals())
@app.route("/comment",methods=['POST', 'GET'])
def comment():
	if request.form:
		nome=request.form.get("nome",None)
		comentario=request.form.get("comentario",None)
		if nome!=None and comentario!=None and re.match(r"^\w+$",nome):
			dao.add(nome,comentario)
	return redirect("/index.html#comments_container")
app.run()