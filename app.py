import os
from flask import Flask, render_template, request, jsonify
from werkzeug.utils import secure_filename
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import PyPDF2
import docx

# Flask setup
app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = "uploads"
os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# Extract text from DOCX
def extract_text_from_docx(file_path):
    doc = docx.Document(file_path)
    return " ".join([p.text for p in doc.paragraphs])

# Skill matching
def extract_skills(text, skills_list):
    found = [skill for skill in skills_list if skill.lower() in text.lower()]
    return found

# Load skills list
with open("skills.txt", "r") as f:
    SKILLS = [line.strip() for line in f if line.strip()]

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        job_desc = request.form["jobdesc"]
        resume_file = request.files["resume"]

        if not resume_file:
            return render_template("index.html", error="No file uploaded")

        # Save resume
        filename = secure_filename(resume_file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        resume_file.save(filepath)

        # Extract resume text
        if filename.endswith(".pdf"):
            resume_text = extract_text_from_pdf(filepath)
        elif filename.endswith(".docx"):
            resume_text = extract_text_from_docx(filepath)
        else:
            return render_template("index.html", error="Only PDF and DOCX supported")

        # Calculate similarity
        vectorizer = TfidfVectorizer().fit([job_desc, resume_text])
        tfidf_matrix = vectorizer.transform([job_desc, resume_text])
        similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0] * 100

        # Extract skills
        matched_skills = extract_skills(resume_text, SKILLS)

        result = {
            "match_score": round(similarity, 2),
            "matched_skills": matched_skills
        }

        return render_template("index.html", result=result)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
