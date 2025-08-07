
from backend.matcher import match_resumes

def test_similarity():
    jd = "Looking for Python developer"
    resumes = [("r1.txt", b"Expert in Python and Django"), ("r2.txt", b"Marketing specialist")]
    results = match_resumes(jd, resumes)
    assert results[0]["score"] > results[1]["score"]
