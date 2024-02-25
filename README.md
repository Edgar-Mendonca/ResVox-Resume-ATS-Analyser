# <img align="center" src="https://raw.githubusercontent.com/Edgar-Mendonca/ResVox-Resume-ATS-Analyser/main/static/images/logo.jpeg" height="50" width="50" /></a> ResuVox: Resume ATS Analyser

## Description
ResuVox is a Flask-based web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). ATS are software systems used by employers to manage the recruitment process by scanning and filtering resumes based on specific criteria. ResuVox analyses resumes and job descriptions to provide insights into keyword matching, readability scores, and other relevant metrics to increase the chances of passing through ATS filters.

## Features
- **ATS Score Calculation:** Calculate the compatibility score between a resume and a job description based on keyword matching using TF-IDF analysis and cosine similarity.
- **Skills Matching:** Identify matching and missing skills between the resume and job description to help users tailor their resumes to specific job requirements.
- **Readability Assessment:** Provide readability scores and insights using various readability formulas such as Flesch-Kincaid and Gunning Fog to ensure the resume is easily understandable.
- **Additional Information:** Offer explanations of grading systems used for readability assessment, helping users understand the significance of each metric.

## What This App Offers
ResuVox aims to simplify the process of optimizing resumes for ATS by providing a comprehensive analysis of keyword matching, skills alignment, and readability metrics. Whether you're a seasoned professional or a recent graduate, ResuVox can help you create resumes that stand out in the competitive job market and increase your chances of landing interviews.

## Usage
To use ResuVox, simply navigate to the application URL, paste your resume and job description, and click the "Analyse" button. Review the analysis results to gain insights into keyword matching, skills alignment, and readability scores, and make necessary adjustments to optimize your resume for ATS.

## Requirements
To run ResuVox locally, you'll need to have the following installed:
- Python (version 3.x)
- Flask
- nltk
- scikit-learn
- textstat

To run this locally, you'll need to have Python installed on your machine. It's recommended to set up a virtual environment to isolate the project dependencies. Here's how you can do it:
```bash
python -m venv venv
```
Activate the Virtual Environment: Depending on your operating system, activate the virtual environment using one of the following commands:
- On Windows:
```bash
venv\Scripts\activate
```

- On macOS and Linux:
 ```bash
source venv/bin/activate
```

Install the Python dependencies using pip:
```bash
pip install Flask nltk scikit-learn textstat
```

## Built Using

ResuVox ATS is built using the following technologies:

<div align="center">
    <img width="48" height="48" src="https://img.icons8.com/color/48/python--v1.png" alt="python--v1"/>
    <img width="50" height="50" src="https://img.icons8.com/ios/50/flask.png" alt="flask"/>
    <img  width="50" height="50" src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/scikitlearn/scikitlearn-original.svg" />
    <img src="https://img.icons8.com/color/48/000000/html-5--v1.png" alt="HTML5" title="HTML5" width="48" height="48"/>
    <img src="https://img.icons8.com/color/48/000000/css3.png" alt="CSS3" title="CSS3" width="48" height="48"/>
    <img src="https://img.icons8.com/color/48/000000/javascript--v1.png" alt="JavaScript" title="JavaScript" width="48" height="48"/>
    <img src="https://img.icons8.com/color/48/000000/bootstrap.png" alt="Bootstrap" title="Bootstrap" width="48" height="48"/>
    <img src="https://upload.wikimedia.org/wikipedia/commons/0/04/ChatGPT_logo.svg" alt="ChatGPT Logo" title="ChatGPT Logo" width="48" height="48"/>
</div>

## Support

If you find ResuVox ATS helpful and would like to support its development, you can contribute by buying me a coffee or donating via PayPal:

<div align="center">
<a href="https://www.buymeacoffee.com/edgarmendonca" target="_blank"><img width="171" height="48" src="https://raw.githubusercontent.com/Edgar-Mendonca/ProfileCraft/21fc45fc8cce9bc2e10a07acd8185b904bce84dd/static/icons/bmc-button.svg" alt=""/></a>&nbsp;&nbsp;&nbsp;<a href="#" target="_blank"><img width="48" height="48" src="https://img.icons8.com/color/48/000000/paypal--v1.png" alt=""/></a>
</div>

## License
This project is licensed under the [MIT License](LICENSE).

