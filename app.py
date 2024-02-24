from flask import Flask, render_template, request
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import textstat


app = Flask(__name__)

def extract_skills(text):
    # Tokenize the text into words
    words = word_tokenize(text.lower())

    # Remove common English stopwords
    stop_words = set(stopwords.words('english'))
    filtered_words = [word for word in words if word.isalnum() and word not in stop_words]

    return set(filtered_words)

def calculate_ats_score_and_skills(resume, job_description):
    # Combine resume and job description for TF-IDF analysis
    corpus = [resume, job_description]

    # Use TF-IDF vectorizer
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(corpus)

    # Calculate cosine similarity
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)

    # The similarity score is stored at cosine_sim[0][1]
    ats_score = round(cosine_sim[0][1] * 100, 2)

    # Get the feature names from the vectorizer (words in the corpus)
    feature_names = vectorizer.get_feature_names_out()

    # Remove common words, punctuation, and numbers
    stop_words = set(stopwords.words('english') + list(string.punctuation))
    filtered_feature_names = [word for word in feature_names if word.lower() not in stop_words and not word.isdigit()]

    # Get the keywords present in the job description but not in the resume
    missing_keywords = [keyword for keyword in filtered_feature_names if keyword not in word_tokenize(resume.lower())]

    # Extract skills from the resume and job description
    resume_skills = extract_skills(resume)
    job_skills = extract_skills(job_description)

    # Calculate matching and missing skills
    matching_skills = resume_skills.intersection(job_skills)
    missing_skills = job_skills - resume_skills

    return ats_score, missing_keywords, matching_skills, missing_skills

def assess_formatting_and_readability(resume):
    # Calculate various readability scores
    readability_scores = {
        'flesch_reading_ease': textstat.flesch_reading_ease(resume),
        'flesch_kincaid_grade': textstat.flesch_kincaid_grade(resume),
        'gunning_fog': textstat.gunning_fog(resume),
        'smog_index': textstat.smog_index(resume),
        'coleman_liau_index': textstat.coleman_liau_index(resume),
        'automated_readability_index': textstat.automated_readability_index(resume),
        'linsear_write_formula': textstat.linsear_write_formula(resume),
        'dale_chall_readability_score': textstat.dale_chall_readability_score(resume),
        'readability_consensus': textstat.text_standard(resume),
        'spache_readability_formula': textstat.spache_readability(resume),
        'mcalpine_eflaw_readability_score': textstat.mcalpine_eflaw(resume),
    }

    # Calculate reading time using textstat
    reading_time = textstat.reading_time(resume, ms_per_char=3)

    # Calculate aggregates and averages
    syllable_count = textstat.syllable_count(resume)
    lexicon_count = textstat.lexicon_count(resume)
    sentence_count = textstat.sentence_count(resume)
    character_count = len(resume)
    letter_count = textstat.letter_count(resume)
    polysyllable_count = textstat.polysyllabcount(resume)
    monosyllable_count = textstat.monosyllabcount(resume)

    aggregates_averages = {
        'Syllable Count': syllable_count,
        'Lexicon Count': lexicon_count,
        'Sentence Count': sentence_count,
        'Character Count': character_count,
        'Letter Count': letter_count,
        'Polysyllable Count': polysyllable_count,
        'Monosyllable Count': monosyllable_count,
    }

    return readability_scores, reading_time, aggregates_averages

    

@app.route('/', methods=['GET', 'POST'])
def index():
    score = None
    resume = ""
    job_description = ""
    missing_keywords = []
    matching_skills = set()
    missing_skills = set()
    readability_scores = {}
    reading_time = None
    aggregates_averages = {}  # Initialize aggregates_averages

    if request.method == 'POST':
        resume = request.form['resume']
        job_description = request.form['job_description']

        # Calculate ATS score and get missing keywords, matching skills, and missing skills
        score, missing_keywords, matching_skills, missing_skills = calculate_ats_score_and_skills(resume, job_description)

        # Assess formatting and readability
        readability_scores, reading_time, aggregates_averages = assess_formatting_and_readability(resume)

    return render_template('index.html', resume=resume, job_description=job_description, score=score,
                           missing_keywords=missing_keywords, matching_skills=matching_skills,
                           missing_skills=missing_skills, readability_scores=readability_scores,
                           reading_time=reading_time, aggregates_averages=aggregates_averages)


if __name__ == '__main__':
    app.run(debug=True)
