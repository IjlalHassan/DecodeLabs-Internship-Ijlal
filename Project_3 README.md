# Career Path Recommender
### DecodeLabs Industrial Training — Project 3 | Batch 2026

A content-based recommendation engine that maps your current skills to the most relevant tech career paths. Built from scratch using only Python's built-in `math` module — no external libraries, no shortcuts.

---

## What This Project Does

You enter your skills. The system tells you:

- Which tech roles match your profile and by how much
- What percentage of each role's requirements you already cover
- Exactly which skills you need to learn next
- A priority learning list based on what's most in-demand across your top matches

---

## How It Works — The Full Pipeline

### Step 1: Dataset (Item Database)
Ten tech job roles are stored as lists of required skills. Each role is treated as a "document" in the recommendation engine's vocabulary.

### Step 2: Shared Vocabulary
All unique skills across all roles are extracted into a single sorted list. This is the shared vector space. Both user input and job roles must map to this same space for the math to work.

### Step 3: TF — Term Frequency
For any list of skills, TF measures how frequently each skill appears relative to the total number of skills in that list.

```
TF(skill) = count of skill / total skills in document
```

### Step 4: IDF — Inverse Document Frequency
Skills that appear in many roles (like `python`) are common and less distinctive. Skills that appear in only one or two roles (like `huggingface`) are highly specific. IDF penalizes common skills and rewards rare ones.

```
IDF(skill) = log( total roles / (1 + roles containing skill) )
```

### Step 5: TF-IDF Vectorization
Each skill list is converted into a numerical vector where every dimension represents one skill from the vocabulary. The value at each dimension is `TF × IDF`. Skills not present get a value of zero.

### Step 6: Cosine Similarity
The user's vector is compared against every job role's vector using cosine similarity. This measures the angle between two vectors — not their size. So a user with 3 skills and a role with 8 skills can still score highly if their directions are aligned.

```
cosine(A, B) = (A · B) / (||A|| × ||B||)
```

Score of 1.0 means perfect alignment. Score of 0.0 means no overlap at all.

### Step 7: Gap Analysis
After scoring, the system computes which required skills for a role the user does not yet have. This produces the "Skills to learn next" list — the actual useful output beyond a raw score.

### Step 8: Ranking and Output
All roles are sorted by score in descending order. The top N results are shown with their match score, coverage percentage, and skill gaps. A bonus section aggregates the most frequently missing skills across all top results to produce a single priority learning list.

---

## Supported Skills

```
aws, azure, bash, calculus, ci-cd, computer-vision, cryptography,
css, deep-learning, docker, ethical-hacking, excel, firewalls, git,
html, huggingface, image-processing, java, javascript, kubernetes,
linear-algebra, linux, matplotlib, model-deployment, networking,
nlp, nodejs, numpy, opencv, pandas, powerbi, pytorch, react,
restapi, scikit-learn, sql, statistics, system-design, tableau,
tensorflow, terraform, transformers, vulnerability-assessment
```

---

## Supported Career Roles

| Role | Core Skills |
|---|---|
| Machine Learning Engineer | python, tensorflow, scikit-learn, statistics |
| Web Developer | html, css, javascript, react, nodejs |
| Data Analyst | python, sql, pandas, tableau, powerbi |
| DevOps Engineer | docker, kubernetes, aws, ci-cd, linux |
| AI Research Scientist | pytorch, nlp, computer-vision, calculus |
| Backend Developer | python, java, restapi, system-design |
| Cybersecurity Analyst | networking, ethical-hacking, cryptography |
| Cloud Architect | aws, azure, terraform, kubernetes |
| NLP Engineer | nlp, transformers, huggingface, pytorch |
| Computer Vision Engineer | opencv, deep-learning, image-processing |

---

## How to Run

No installation needed. Python 3 is all you need.

```bash
python recommender.py
```

You will see the full list of available skills. Enter at least 3, comma-separated:

```
Your skills: python, sql, statistics, pandas, matplotlib
```

Then choose how many recommendations you want (default is 3).

---

## Sample Output

```
=======================================================
   TOP 3 CAREER MATCHES FOR YOUR SKILL PROFILE
=======================================================

Rank #1 — Data Analyst
  Match Score : 64.1%
  You already cover 62.5% of required skills
  Skills to learn next: excel, powerbi, tableau

Rank #2 — Machine Learning Engineer
  Match Score : 26.0%
  You already cover 37.5% of required skills
  Skills to learn next: linear-algebra, model-deployment, numpy, scikit-learn, tensorflow

Rank #3 — Backend Developer
  Match Score : 12.4%
  You already cover 25.0% of required skills
  Skills to learn next: docker, git, java, nodejs, restapi, system-design

=======================================================
  BONUS: Skills most in-demand across all top roles
=======================================================
  Priority order: excel, tableau, powerbi, numpy, model-deployment
```

---

## Technical Concepts Applied

| Concept | Where Used |
|---|---|
| TF-IDF Weighting | Feature extraction for skills |
| Cosine Similarity | Comparing user vector to role vectors |
| Content-Based Filtering | No user history needed, pure attribute matching |
| Gap Analysis | Set difference between user skills and role requirements |
| Top-N Filtering | Prevents choice overload, returns ranked short list |

---

## Why No External Libraries?

This project is built using only Python's `math` module. No `sklearn`, no `numpy`, no `scipy`. Every calculation — TF, IDF, dot product, vector magnitude — is implemented manually. This is intentional. Understanding what happens under the hood is more valuable than calling `cosine_similarity()` from a library and not knowing what it actually does.

---

## Project Structure

```
recommender.py   — Full recommendation engine (single file)
README.md        — This file
```

---

## Built For

DecodeLabs Industrial Training Kit | Artificial Intelligence Track | Project 3
