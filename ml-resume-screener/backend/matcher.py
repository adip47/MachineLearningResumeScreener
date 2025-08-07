
from sentence_transformers import SentenceTransformer, util

model = SentenceTransformer('paraphrase-MiniLM-L6-v2')

def match_resumes(jd_text, resumes):
    jd_emb = model.encode(jd_text, convert_to_tensor=True)
    results = []

    for name, content in resumes:
        resume_emb = model.encode(content.decode(), convert_to_tensor=True)
        score = util.pytorch_cos_sim(jd_emb, resume_emb).item()
        results.append({"name": name, "score": round(score, 3)})

    return sorted(results, key=lambda x: x['score'], reverse=True)
