from flask import Flask, request, render_template, redirect, url_for
import openai
import os
from pdfminer.high_level import extract_text

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = 'uploads'

# Ensure the API key is set from the environment variable
api_key = os.getenv("OPENAI_API_KEY")
if not api_key:
    raise ValueError("No API key found in environment variables. Please set the OPENAI_API_KEY environment variable.")
openai.api_key = api_key

if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'file' not in request.files:
            return redirect(request.url)
        file = request.files['file']
        if file.filename == '':
            return redirect(request.url)
        if file:
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
            file.save(file_path)
            result, score = analyze_pdf(file_path)
            os.remove(file_path)
            return render_template('index.html', result=result, score=score)
    return render_template('index.html')

def analyze_pdf(file_path):
    try:
        text = extract_text(file_path)
        if "LinkedIn" not in text:
            return "Wrong PDF upload, upload only your LinkedIn profile page PDF.", "N/A"

        prompt = (
            "Analyze the following LinkedIn profile and provide a score out of 100. The score should reflect the "
            "overall quality of the profile, including the completeness of the information, the relevance of the "
            "skills and experience, and the professionalism of the presentation. After providing the score, please "
            "summarize the strengths, recommendations for improvement, and provide final feedback:\n\n"
            f"{text}"
        )

        response = openai.ChatCompletion.create(
            model="gpt-4-turbo",
            messages=[
                {"role": "system", "content": "You are an expert in analyzing LinkedIn profiles."},
                {"role": "user", "content": prompt}
            ]
        )

        analysis = response.choices[0].message['content']
        print("Analysis Output: ", analysis)  # Debugging output
        score = extract_score(analysis)

        return format_analysis(analysis, score), score
    except Exception as e:
        print(f"Error during analysis: {e}")
        return f"Error processing the PDF: {e}", "N/A"

def extract_score(analysis):
    import re
    match = re.search(r"(\d+)\s*/\s*100", analysis)
    if match:
        return f"{match.group(1)}%"
    else:
        return "N/A"

def format_analysis(analysis, score):
    strengths = ""
    recommendations = ""
    feedback = ""

    lines = analysis.split('\n')

    current_section = ""
    for line in lines:
        line = line.strip()
        if "Strengths:" in line:
            current_section = "strengths"
            strengths += f"<strong>{line}</strong><ol style='list-style-type:none;'>"
        elif "Recommendations for Improvement:" in line:
            if current_section == "strengths":
                strengths += "</ol>"
            current_section = "recommendations"
            recommendations += f"<strong>{line}</strong><ol style='list-style-type:none;'>"
        elif "Feedback:" in line:
            if current_section == "recommendations":
                recommendations += "</ol>"
            current_section = "feedback"
            feedback += f"<strong>{line}</strong><p>"
        else:
            if current_section == "strengths":
                strengths += f"<li>{line}</li>"
            elif current_section == "recommendations":
                recommendations += f"<li>{line}</li>"
            elif current_section == "feedback":
                feedback += f"{line} "

    if strengths:
        strengths += "</ol>"
    if recommendations:
        recommendations += "</ol>"
    if feedback:
        feedback += "</p>"

    formatted_analysis = (
        f"<div class='section'><div class='box'>{strengths}</div></div>"
        f"<div class='section'><div class='box'>{recommendations}</div></div>"
        f"<div class='section'><div class='box'>{feedback}</div></div>"
    )

    return formatted_analysis

@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store'
    return response

if __name__ == '__main__':
    app.run(debug=True)























