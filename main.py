import parser
from fastapi import FastAPI, Form
from fastapi.responses import FileResponse, HTMLResponse

app = FastAPI()

@app.get("/")
def main_page():
    return FileResponse("temp/index.html")

@app.post("/submit")
def submit_page(urls_area: str = Form(...), sort_by: str = Form(...)):
    urls_lst = parser.create_urls_lst(urls_area)
    sorted_videos_information = parser.create_sorted_videos_information_dict(urls_lst, sort_by)
    if type(sorted_videos_information) is dict:
        return sorted_videos_information
    elif type(sorted_videos_information) is str:
        return HTMLResponse(sorted_videos_information, status_code=422)