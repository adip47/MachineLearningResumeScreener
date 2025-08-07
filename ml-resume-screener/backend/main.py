
from fastapi import FastAPI, UploadFile, File
from matcher import match_resumes
import os

app = FastAPI()

@app.post("/match/")
async def match(jd: UploadFile = File(...), resumes: list[UploadFile] = File(...)):
    jd_text = await jd.read()
    resumes_texts = [(res.filename, await res.read()) for res in resumes]
    results = match_resumes(jd_text.decode(), resumes_texts)
    return {"results": results}
