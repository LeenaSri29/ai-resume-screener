# AI Resume Screener

AI Resume Screener is a web-based application that leverages Artificial Intelligence and Natural Language Processing (NLP) to automate resume screening for recruiters. It analyzes uploaded resumes against a job description, evaluates skills, keyword relevance, and overall fit, and generates a downloadable PDF report for each candidate.

## Features

- Upload multiple resumes (PDF/DOCX)
- Extract and compare skills from resumes and job descriptions
- Calculate similarity and skill match scores
- Generate professional PDF reports for each candidate
- Modern and responsive frontend using Bootstrap
- Handles long text and large resumes efficiently

## Tech Stack

- **Backend:** Python, Flask, scikit-learn, spaCy
- **Frontend:** HTML, Bootstrap
- **PDF Generation:** FPDF
- **Document Parsing:** pdfminer.six, python-docx

## Installation

1. Clone the repository:

```bash
git clone https://github.com/your-username/ai-resume-screener.git
cd ai-resume-screener
Create and activate a virtual environment:

bash
Copy code
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
flask run
Open http://127.0.0.1:5000 in your browser.

Usage
Paste the job description in the textarea.

Upload one or more resumes.

Click Analyze Resumes.

View results and download PDF reports.


## Screenshots

![Screenshot 1](images/Screenshot%202025-09-08%20164901.png)
![Screenshot 2](images/Screenshot%202025-09-08%20165003.png)
![Screenshot 3](images/Screenshot%202025-09-08%20165017.png)

License
This project is licensed under the MIT License. See the LICENSE file for details.

Copyright (c) 2025 Thupakula Leena Sri

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
