from fastapi import FastAPI, Form
from fastapi.responses import FileResponse
import tempfile
from ai_generator import generate_assignment, generate_proposal
from file_builder import make_docx, make_pdf

app = FastAPI(title="AI Assignment & Proposal Maker")

@app.get("/")
def root():
    return {"message": "AI Assignment & Proposal Maker API is running 🚀"}

@app.post("/generate")
async def generate(
    mode: str = Form(...),  # "assignment" or "proposal"
    topic: str = Form(...),
    subject: str = Form("General"),
    format: str = Form("pdf")  # "pdf" or "docx"
):
    """
    mode: assignment / proposal
    topic: text topic or input
    subject: optional
    format: pdf / docx
    """
    # Step 1: Generate AI content
    if mode == "proposal":
        generated = generate_proposal(topic, subject)
    else:
        generated = generate_assignment(topic, subject)

    # Step 2: Create file
    output_file = make_docx(generated) if format == "docx" else make_pdf(generated)

    return FileResponse(output_file, filename=f"{mode}.{format}")
