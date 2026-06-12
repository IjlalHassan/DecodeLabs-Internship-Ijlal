import math

dataset = {
    "Machine Learning Engineer": ["python", "numpy", "pandas", "scikit-learn", "tensorflow", "statistics", "linear-algebra", "model-deployment"],
    "Web Developer": ["html", "css", "javascript", "react", "nodejs", "sql", "restapi", "git"],
    "Data Analyst": ["python", "sql", "excel", "pandas", "matplotlib", "statistics", "powerbi", "tableau"],
    "DevOps Engineer": ["linux", "docker", "kubernetes", "aws", "ci-cd", "bash", "git", "networking"],
    "AI Research Scientist": ["python", "tensorflow", "pytorch", "linear-algebra", "calculus", "statistics", "nlp", "computer-vision"],
    "Backend Developer": ["python", "java", "sql", "restapi", "docker", "git", "nodejs", "system-design"],
    "Cybersecurity Analyst": ["networking", "linux", "python", "ethical-hacking", "firewalls", "cryptography", "bash", "vulnerability-assessment"],
    "Cloud Architect": ["aws", "azure", "docker", "kubernetes", "networking", "terraform", "ci-cd", "system-design"],
    "NLP Engineer": ["python", "nlp", "pytorch", "tensorflow", "transformers", "statistics", "linear-algebra", "huggingface"],
    "Computer Vision Engineer": ["python", "opencv", "pytorch", "tensorflow", "linear-algebra", "computer-vision", "deep-learning", "image-processing"],
}

all_skills = sorted(set(skill for skills in dataset.values() for skill in skills))

def compute_tf(skills):
    tf = {}
    total = len(skills)
    for skill in skills:
        tf[skill] = tf.get(skill, 0) + 1
    for skill in tf:
        tf[skill] = tf[skill] / total
    return tf

def compute_idf(dataset):
    total_docs = len(dataset)
    idf = {}
    for skill in all_skills:
        docs_with_skill = sum(1 for skills in dataset.values() if skill in skills)
        idf[skill] = math.log(total_docs / (1 + docs_with_skill))
    return idf

def vectorize(skills, idf):
    tf = compute_tf(skills)
    vector = []
    for skill in all_skills:
        tfidf = tf.get(skill, 0) * idf.get(skill, 0)
        vector.append(tfidf)
    return vector

def cosine_similarity(vec_a, vec_b):
    dot = sum(a * b for a, b in zip(vec_a, vec_b))
    mag_a = math.sqrt(sum(a ** 2 for a in vec_a))
    mag_b = math.sqrt(sum(b ** 2 for b in vec_b))
    if mag_a == 0 or mag_b == 0:
        return 0.0
    return dot / (mag_a * mag_b)

def gap_analysis(user_skills, role_skills):
    user_set = set(user_skills)
    role_set = set(role_skills)
    missing = role_set - user_set
    already_have = role_set & user_set
    coverage = len(already_have) / len(role_set) * 100
    return missing, round(coverage, 1)

def recommend(user_skills, top_n=3):
    idf = compute_idf(dataset)
    user_vec = vectorize(user_skills, idf)

    if all(v == 0 for v in user_vec):
        print("\nNone of your skills matched our database. Try different skill names.\n")
        return

    scores = []
    for role, role_skills in dataset.items():
        role_vec = vectorize(role_skills, idf)
        score = cosine_similarity(user_vec, role_vec)
        missing, coverage = gap_analysis(user_skills, role_skills)
        scores.append((role, score, missing, coverage))

    scores.sort(key=lambda x: x[1], reverse=True)
    top = scores[:top_n]

    print("\n" + "="*55)
    print("   TOP {} CAREER MATCHES FOR YOUR SKILL PROFILE".format(top_n))
    print("="*55)

    for i, (role, score, missing, coverage) in enumerate(top, 1):
        print("\nRank #{} — {}".format(i, role))
        print("  Match Score : {:.1f}%".format(score * 100))
        print("  You already cover {:.1f}% of required skills".format(coverage))
        if missing:
            print("  Skills to learn next: {}".format(", ".join(sorted(missing))))
        else:
            print("  You have all the skills for this role!")

    print("\n" + "="*55)
    print("  BONUS: Skills most in-demand across all top roles")
    print("="*55)
    all_missing = {}
    for _, _, missing, _ in top:
        for skill in missing:
            all_missing[skill] = all_missing.get(skill, 0) + 1
    priority = sorted(all_missing.items(), key=lambda x: x[1], reverse=True)
    if priority:
        print("  Priority order: {}".format(", ".join(s for s, _ in priority[:5])))
    print()

def main():
    print("\n" + "="*55)
    print("     CAREER PATH RECOMMENDER — DecodeLabs P3")
    print("   Powered by TF-IDF + Cosine Similarity Engine")
    print("="*55)
    print("\nAvailable skills you can enter:")
    for i in range(0, len(all_skills), 5):
        print("  " + ", ".join(all_skills[i:i+5]))

    print("\nEnter at least 3 skills (comma-separated):")
    raw = input("Your skills: ").strip().lower()
    user_skills = [s.strip() for s in raw.split(",") if s.strip()]

    if len(user_skills) < 3:
        print("You need at least 3 skills. The PDF literally said so.")
        return

    how_many = input("\nHow many recommendations do you want? (default 3): ").strip()
    top_n = int(how_many) if how_many.isdigit() else 3

    recommend(user_skills, top_n)

if __name__ == "__main__":
    main()