from fastapi import FastAPI
from pydantic import BaseModel
from planner import VacationRequest, make_plan, save_reports
from fastapi.responses import FileResponse

# Create an API Server using FastAPI
app = FastAPI(title="AI Vacation Planner")


class VacationRequestIn(BaseModel):
    name: str
    days: int
    budget: int
    style: str
    destination_type: str
    constraints: str = ""

# Method POST   /plan
@app.post("/plan")
def generate_plan(req: VacationRequestIn):
    plan = make_plan(VacationRequest(**req.dict()))
    save_reports(plan)

    # return the data : preview, json url and txt url to user
    return {
        "preview": plan["plan_text"][:300],
        "download_txt": "/download/txt",
        "download_json": "/download/json"
    }


# Method GET /download/txt
# if user open /download/txt
# it will goes here
# it will return the file vacation_report.txt

@app.get("/download/txt")
def download_txt():
    return FileResponse("vacation_report.txt")

# Method GET /download/json
# if user open /download/json
# it will goes here
# it will return the file vacation_report.json

@app.get("/download/json")
def download_json():
    return FileResponse("vacation_report.json")
