from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import numpy as np
import textblob
import requests


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

     # Preprocessing response for better formatting
    processed_response = r.text

    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response = processed_response + "</h4>"  # Close the final <h4> tag

    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"

    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"

    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "What are my best loan options for home financing?"
@app.route("/house_loan_options", methods=["GET", "POST"])
def house_loan_options():
    q = "What are my best loan options for home financing?"
    r = model.generate_content(q)
 # Preprocessing response for better formatting
    processed_response = r.text

    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response = processed_response + "</h4>"  # Close the final <h4> tag

    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"

    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "How can I figure out the right budget for my new home?"
@app.route("/house_budget_affordability", methods=["GET", "POST"])
def house_budget_affordability():
    q = "How can I figure out the right budget for my new home?"
    r = model.generate_content(q)
 # Preprocessing response for better formatting
    processed_response = r.text

    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response = processed_response + "</h4>"  # Close the final <h4> tag

    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"

    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"

    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "What types of home insurance should I consider?"
@app.route("/house_insurance_options", methods=["GET", "POST"])
def house_insurance_options():
    q = "What types of home insurance should I consider?"
    r = model.generate_content(q)
 # Preprocessing response for better formatting
    processed_response = r.text

    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response = processed_response + "</h4>"  # Close the final <h4> tag

    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"

    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"

    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for handling custom house purchase questions
@app.route("/house_custom_question", methods=["GET", "POST"])
def house_custom_question():
    user_question = request.form['q']  # Custom question entered by the user
    r = model.generate_content(user_question)
 # Preprocessing response for better formatting
    processed_response = r.text

    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response = processed_response + "</h4>"  # Close the final <h4> tag

    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"

    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return render_template("house_custom_question_reply.html", r=processed_response)

# Dummy profiles, replace with actual profile data if needed
profiles = {
    1: {"name": "Profile 1", "risk_tolerance": "low", "investment_goal": "retirement"},
    2: {"name": "Profile 2", "risk_tolerance": "high", "investment_goal": "growth"},
    3: {"name": "Profile 3", "risk_tolerance": "moderate", "investment_goal": "income"}
}
# Function to get AI investment suggestions using a simulated API call
def get_ai_suggestion(profile):
    api_url = "https://api.makersuite.google.com/investment_suggestions"  # Example API URL
    payload = {"profile": profile}
    return f"Based on {profile['name']} with a {profile['risk_tolerance']} risk tolerance, we suggest focusing on {profile['investment_goal']}."
    
# Route to handle profile suggestion retrieval
@app.route('/get_suggestions/<int:profile_id>', methods=['POST'])
def get_suggestions(profile_id):
    profile = profiles.get(profile_id)
    if profile:
        suggestion = get_ai_suggestion(profile)
        return render_template('AI_Powered_Investment_Suggestions.html', suggestion=suggestion)
    else:
        return render_template('AI_Powered_Investment_Suggestions.html', suggestion="Profile not found")

# Main route for displaying the AI-powered page
@app.route('/ai-suggestions')
def ai_suggestions():
    return render_template('AI_Powered_Investment_Suggestions.html', suggestion="")

if __name__ == "__main__":
    app.run()
