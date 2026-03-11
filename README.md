# ECE324 Final Project — Indian Political Manifesto Analysis

Analysis of Indian political party manifestos (BJP, INC) using text embeddings, TF-IDF, and dimensionality reduction.

## Setup

```bash
python3 -m venv .venv
source .venv/bin/activate   # or: .venv\Scripts\activate on Windows
pip install -r requirements.txt
```

For the notebook you also need: `sentence-transformers`, `umap-learn`, `jupyter`, `ipywidgets` (see notebook imports or install with `pip install sentence-transformers umap-learn jupyter ipywidgets`).

## Repo layout

- **`pdf_data/`** — Source PDF manifestos (`BJP_2009.pdf`, `BJP_2014.pdf`, `INC_2009.pdf`, `INC_2014.pdf`).
- **`data/`** — Extracted plain-text manifestos (`.txt`), one file per party and year.
- **`preprocess.py`** — Loads a PDF with PyMuPDF (`fitz`), extracts text page-by-page, writes a single `.txt` file. Edit `pdf_path` and `txt_output` at the top to process a different PDF.
- **`p1.ipynb`** — Main analysis: loads manifestos from `data/`, chunks text (~300 words), embeds with SentenceTransformer (e.g. MPNet), reduces with UMAP, and uses TF-IDF / logistic regression for comparison and visualization.

## Workflow

1. Put PDFs in `pdf_data/` and run `preprocess.py` (adjust paths as needed) to refresh `data/*.txt`.
2. Open `p1.ipynb`, run all cells (kernel uses the same env as above). First run will download the sentence-transformers model.
