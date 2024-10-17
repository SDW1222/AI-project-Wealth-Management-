from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np
from textblob import TextBlob

model = genai.GenerativeModel("gemini-1.5-flash")
genai.configure(api_key="AIzaSyCluRjLkwn6IOe4f-dNTlusyuAkDUI7fQo")

app = Flask(__name__)
user_name = ""
flag = 1

@app.route("/", methods=["GET", "POST"])
def index():
    global flag
    flag = 1
    return render_template("index.html")


@app.route("/portfolio",methods=["GET","POST"])
def portfolio():
    return(render_template("portfolio.html"))

@app.route("/portfolio_1",methods=["GET","POST"])
def portfolio_1():
    q = "What are the key factors to consider when balancing a portfolio?"
    r = model.generate_content(q)
    return(render_template("portfolio_1_reply.html",r=r.text))

@app.route("/portfolio_2",methods=["GET","POST"])
def portfolio_2():
    q = "How can I optimize my asset allocation?"
    r = model.generate_content(q)
    return(render_template("portfolio_2_reply.html",r=r.text))

@app.route("/portfolio_3",methods=["GET","POST"])
def portfolio_3():
    q = "What market trends should I watch for?"
    r = model.generate_content(q)
    return(render_template("portfolio_3_reply.html",r=r.text))

@app.route("/portfolio_4",methods=["GET","POST"])
def portfolio_4():
    q = "What's the difference between active and passive portfolio management?"
    r = model.generate_content(q)
    return(render_template("portfolio_4_reply.html",r=r.text))

@app.route("/portfolio_gen",methods=["GET","POST"])
def portfolio_gen():
    q = request.form.get("q")
    r = model.generate_content(q)
    return(render_template("portfolio_gen_reply.html",r=r.text))

