# UG Key Detector (RAG)

RAG‑driven key detection from Ultimate‑Guitar chord pages.

## Getting Started

```bash
# clone
git clone git@github.com:your-username/ug-key-detector.git
cd ug-key-detector

# install
poetry install
poetry shell

# run server
uvicorn app.main:app --reload
# visit http://127.0.0.1:8000/docs
