from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

faq_questions = [
    "What is Python?",
    "What is Machine Learning?",
    "What is NLP?",
    "What is AI?",
    "What is Data Science?"
]

faq_answers = [
    "Python is a popular programming language.",
    "Machine Learning enables computers to learn from data.",
    "NLP stands for Natural Language Processing.",
    "AI stands for Artificial Intelligence.",
    "Data Science is the study of data analysis and insights."
]

vectorizer = TfidfVectorizer()
faq_vectors = vectorizer.fit_transform(faq_questions)

user_question = input("Ask a question: ")

user_vector = vectorizer.transform([user_question])

similarity = cosine_similarity(user_vector, faq_vectors)

index = similarity.argmax()

print("Bot:", faq_answers[index])
