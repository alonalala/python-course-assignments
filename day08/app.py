from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field
from business_logic import calculate_rolling_metrics

app = FastAPI(
    title="Cis-Regulatory Sequence Profiler API",
    description="Web API to analyze DNA sequences for rolling GC% and CpG distribution."
)

class SequenceAnalysisRequest(BaseModel):
    sequence: str = Field(..., min_length=10, description="DNA sequence string (A, T, C, G)")
    window_size: int = Field(50, ge=10, le=500, description="Sliding window size in base pairs")

@app.get("/")
def read_root():
    return {"message": "Welcome to the API. Go to /docs for interactive documentation."}

@app.post("/analyze")
def analyze_sequence(request: SequenceAnalysisRequest):
    clean_seq = request.sequence.upper().strip()
    if not all(base in "ATCGN" for base in clean_seq):
        raise HTTPException(status_code=420, detail="Invalid characters detected. Sequence must only contain A, T, C, G, or N.")
        
    if request.window_size > len(clean_seq):
        raise HTTPException(status_code=400, detail="Window size cannot be larger than the sequence length.")

    # Calls the shared function from business_logic.py
    profile_data = calculate_rolling_metrics(clean_seq, request.window_size)
    
    return {
        "sequence_length": len(clean_seq),
        "window_size": request.window_size,
        "profile": profile_data
    }