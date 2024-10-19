from flask import Flask, render_template, request, jsonify
import google.generativeai as genai
import os
import numpy as np
import textblob
import requests
import random
import markdown

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
    processed_response = r.text
    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response += "</h4>"  # Close the final <h4> tag
    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Handle multiple parts of the response (if needed)
    sections = processed_response.split("\n\n")  # Split by double newlines
    if len(sections) > 1:
        processed_response = sections[-1]  # Take the last section if there are multiple parts
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "What are my best loan options for home financing?"
@app.route("/house_loan_options", methods=["GET", "POST"])
def house_loan_options():
    q = "What are my best loan options for home financing?"
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
    processed_response = r.text
    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response += "</h4>"  # Close the final <h4> tag
    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Handle multiple parts of the response (if needed)
    sections = processed_response.split("\n\n")  # Split by double newlines
    if len(sections) > 1:
        processed_response = sections[-1]  # Take the last section if there are multiple parts
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "How can I figure out the right budget for my new home?"
@app.route("/house_budget_affordability", methods=["GET", "POST"])
def house_budget_affordability():
    q = "How can I figure out the right budget for my new home?"
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
    processed_response = r.text
    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response += "</h4>"  # Close the final <h4> tag
    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Handle multiple parts of the response (if needed)
    sections = processed_response.split("\n\n")  # Split by double newlines
    if len(sections) > 1:
        processed_response = sections[-1]  # Take the last section if there are multiple parts
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return render_template("house_savings_target_reply.html", r=processed_response)

# Route for "What types of home insurance should I consider?"
@app.route("/house_insurance_options", methods=["GET", "POST"])
def house_insurance_options():
    q = "What types of home insurance should I consider?"
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
    processed_response = r.text
    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response += "</h4>"  # Close the final <h4> tag
    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Handle multiple parts of the response (if needed)
    sections = processed_response.split("\n\n")  # Split by double newlines
    if len(sections) > 1:
        processed_response = sections[-1]  # Take the last section if there are multiple parts
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return render_template("house_savings_target_reply.html", r=processed_response)

@app.route("/house_custom_question", methods=["GET", "POST"])
def house_custom_question():
    user_question = request.form['q']  # Custom question entered by the user
    r = model.generate_content(user_question)
    # Preprocessing response to format better for HTML
    processed_response = r.text
    # Convert headings (e.g., '1*', '2*') to <h4> tags
    processed_response = processed_response.replace("1*", "<h4>")
    processed_response = processed_response.replace("2*", "</h4><h4>")
    processed_response = processed_response.replace("3*", "</h4><h4>")
    processed_response = processed_response.replace("4*", "</h4><h4>")
    processed_response += "</h4>"  # Close the final <h4> tag
    # Convert markers (*) to bold and lists where appropriate
    processed_response = processed_response.replace("*", "<strong>")
    processed_response = processed_response.replace("\n- ", "<ul><li>")
    processed_response = processed_response.replace("\n", "</li><li>")
    processed_response += "</li></ul>"
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Handle multiple parts of the response (if needed)
    sections = processed_response.split("\n\n")  # Split by double newlines
    if len(sections) > 1:
        processed_response = sections[-1]  # Take the last section if there are multiple parts
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"

    return render_template("house_custom_question_reply.html", r=processed_response)

# Dummy profiles
profiles = {
    1: {"name": "Profile 1", "risk_tolerance": "low", "investment_goal": "retirement"},
    2: {"name": "Profile 2", "risk_tolerance": "high", "investment_goal": "growth"},
    3: {"name": "Profile 3", "risk_tolerance": "moderate", "investment_goal": "income"}
}

# Function to generate AI-powered investment suggestions
def get_ai_suggestion(profile):
    prompt = ""
    if profile["name"] == "Profile 1":
        prompt = "Provide a detailed, structured recommendation on increasing bond allocation to 40% using proper bullet points, headings, and formatting in markdown."
    elif profile["name"] == "Profile 2":
        prompt = "Provide key considerations for investing in emerging markets. Use bullet points, subheadings, and markdown formatting."
    elif profile["name"] == "Profile 3":
        prompt = "Explain how to reduce risk by diversifying real estate holdings. Use markdown for bullet points and clear steps."

    # Call Gen AI model to generate the content
    r = model.generate_content(prompt)
    
    # Return the AI-generated content in markdown format
    return r.text

# Route to handle suggestions for each profile
@app.route('/get_suggestions/<int:profile_id>', methods=['GET'])
def get_suggestions(profile_id):
    profile = profiles.get(profile_id)
    if profile:
        suggestion_md = get_ai_suggestion(profile)  # Get markdown content from AI
        suggestion_html = markdown.markdown(suggestion_md)  # Convert markdown to HTML
        return render_template('investment_suggestion.html', profile=profile, suggestion=suggestion_html)
    else:
        return "Profile not found", 404

# Main route for displaying the AI-powered page
@app.route('/ai-suggestions')
def ai_suggestions():
    return render_template('AI_Powered_Investment_Suggestions.html', suggestion="")

@app.route("/retirement",methods=["GET","POST"])
def retirement():
    return(render_template("retirement.html"))

@app.route("/retirement_1",methods=["GET","POST"])
def retirement_1():
    q = "What’s the best way to start saving for retirement?"
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
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
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return(render_template("retirement_1.html",r=processed_response))


@app.route("/retirement_2",methods=["GET","POST"])
def retirement_2():
    q = "How can I structure my retirement savings?"
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
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
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return(render_template("retirement_2.html",r=processed_response))

@app.route("/retirement_3",methods=["GET","POST"])
def retirement_3():
    q = "What should I know about taxes in retirement?"
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
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
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return(render_template("retirement_3.html",r=processed_response))

@app.route("/retirement_4",methods=["GET","POST"])
def retirement_4():
    q = "How do I assess my future income needs for retirement?"
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
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
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"
    return(render_template("retirement_4.html",r=processed_response))

@app.route("/retirement_5",methods=["GET","POST"])
def retirement_5():
    return(render_template("retirement_5.html"))

@app.route("/retirement_reply", methods=["GET", "POST"])
def retirement_reply():
    q = request.form.get("q")
    r = model.generate_content(q)
    # Preprocessing response to format better for HTML
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
    # Remove empty list items
    processed_response = processed_response.replace("<li></li>", "")
    # Add paragraph tags for text that isn't part of a list
    processed_response = "<p>" + processed_response.replace("\n\n", "</p><p>") + "</p>"

    return render_template("retirement_reply.html", r=processed_response)


if __name__ == "__main__":
    app.run()
