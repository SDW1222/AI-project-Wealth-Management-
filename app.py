from flask import Flask,render_template,request
import google.generativeai as genai
import os
import numpy as np
import textblob


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



@app.route("/house_planning", methods=["GET", "POST"])
def house_planning():
    return render_template("house_planning.html")  # A main page for house purchase questions if needed

@app.route("/house_savings_target", methods=["GET", "POST"])
def house_savings_target():
    q = "How much should I save for a house down payment?"
    r = model.generate_content(q)

    # Preprocessing response to format better for HTML
    processed_response = r.text.replace("\n", "</p><p>")  # Add paragraph tags
    processed_response = processed_response.replace("Key Points:", "<h4>Key Points:</h4>")  # Add heading
    processed_response = processed_response.replace("Consider:", "<h4>Consider:</h4>")  # Add heading

    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "What are my best loan options for home financing?"
@app.route("/house_loan_options", methods=["GET", "POST"])
def house_loan_options():
    q = "What are my best loan options for home financing?"
    r = model.generate_content(q)
# Preprocessing response to format better for HTML
    processed_response = r.text.replace("\n", "</p><p>")  # Add paragraph tags
    processed_response = processed_response.replace("Key Points:", "<h4>Key Points:</h4>")  # Add heading
    processed_response = processed_response.replace("Consider:", "<h4>Consider:</h4>")  # Add heading

    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "How can I figure out the right budget for my new home?"
@app.route("/house_budget_affordability", methods=["GET", "POST"])
def house_budget_affordability():
    q = "How can I figure out the right budget for my new home?"
    r = model.generate_content(q)
# Preprocessing response to format better for HTML
    processed_response = r.text.replace("\n", "</p><p>")  # Add paragraph tags
    processed_response = processed_response.replace("Key Points:", "<h4>Key Points:</h4>")  # Add heading
    processed_response = processed_response.replace("Consider:", "<h4>Consider:</h4>")  # Add heading

    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "What types of home insurance should I consider?"
@app.route("/house_insurance_options", methods=["GET", "POST"])
def house_insurance_options():
    q = "What types of home insurance should I consider?"
    r = model.generate_content(q)
# Preprocessing response to format better for HTML
    processed_response = r.text.replace("\n", "</p><p>")  # Add paragraph tags
    processed_response = processed_response.replace("Key Points:", "<h4>Key Points:</h4>")  # Add heading
    processed_response = processed_response.replace("Consider:", "<h4>Consider:</h4>")  # Add heading

    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for handling custom house purchase questions
@app.route("/house_custom_question", methods=["GET", "POST"])
def house_custom_question():
    user_question = request.form['q']  # Custom question entered by the user
    r = model.generate_content(user_question)
# Preprocessing response to format better for HTML
    processed_response = r.text.replace("\n", "</p><p>")  # Add paragraph tags
    processed_response = processed_response.replace("Key Points:", "<h4>Key Points:</h4>")  # Add heading
    processed_response = processed_response.replace("Consider:", "<h4>Consider:</h4>")  # Add heading

    return render_template("house_savings_target_reply.html", r=processed_response)


if __name__ == "__main__":
    app.run()

