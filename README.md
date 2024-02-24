# ResuVox: Resume ATS Analyzer

## Description
ResuVox is a Flask-based web application designed to help job seekers optimize their resumes for Applicant Tracking Systems (ATS). ATS are software systems used by employers to manage the recruitment process by scanning and filtering resumes based on specific criteria. ResuVox analyzes resumes and job descriptions to provide insights into keyword matching, readability scores, and other relevant metrics to increase the chances of passing through ATS filters.

## Features
- **ATS Score Calculation:** Calculate the compatibility score between a resume and a job description based on keyword matching using TF-IDF analysis and cosine similarity.
- **Skills Matching:** Identify matching and missing skills between the resume and job description to help users tailor their resumes to specific job requirements.
- **Readability Assessment:** Provide readability scores and insights using various readability formulas such as Flesch-Kincaid and Gunning Fog to ensure the resume is easily understandable.
- **Additional Information:** Offer explanations of grading systems used for readability assessment, helping users understand the significance of each metric.

## What This App Offers
ResuVox aims to simplify the process of optimizing resumes for ATS by providing a comprehensive analysis of keyword matching, skills alignment, and readability metrics. Whether you're a seasoned professional or a recent graduate, ResuVox can help you create resumes that stand out in the competitive job market and increase your chances of landing interviews.

## Usage
To use ResuVox, simply navigate to the application URL, paste your resume and job description, and click the "Analyze" button. Review the analysis results to gain insights into keyword matching, skills alignment, and readability scores, and make necessary adjustments to optimize your resume for ATS.

## Requirements
To run ResuVox locally, you'll need to have the following installed:
- Python (version 3.x)
- Flask
- nltk
- scikit-learn
- textstat

You can install the Python dependencies using pip:
```bash
pip install Flask nltk scikit-learn textstat


## License
This project is licensed under the [MIT License](LICENSE).

