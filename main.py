from typing import Any, Dict

from fastapi import FastAPI, Depends
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.requests import Request
import logging

from process import process, u_list

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"))
templates = Jinja2Templates(directory="static/templates")
logger = logging.getLogger('uvicorn.error')


@app.get("/initial_equations")
async def get_initial_equations():
    return u_list


# Точка входа в приложение
@app.get("/")
async def main(
        request: Request,
        initial_equations=Depends(get_initial_equations)
):
    return templates.TemplateResponse(name="index.html", context={
        "request": request,
        "initial_equations": initial_equations,
        "faks": ["S", "F", "G", "T", "A", "D", "I", "P", "C"],
        "equations": [
            "F1s", "F1x8", "F2s", "F2x8", "F2x1", "F2x7", "F3x8", "F3x1", "F3x7", "F4x8",
            "F4x7", "F4x1", "F5s", "F5x1", "F5x7", "F6s", "F6x8", "F7x1", "F8s", "F8x4",
            "F9s", "F9x1", "F9x7", "F10s", "F10x1", "F10x7", "F11s", "F11x6", "F12x11"
        ]
    })


# Метод обработки введенных пользователем значений. Возвращает статус в виде строки. Если статус = "Выполнено",
# то на других страницах будут отображаться нарисованные графики. Пока этот метод не вызван, графики отображаться не должны
@app.post("/draw_graphics")
async def draw_graphics(body: Dict[Any, Any]):
    try:
        process(body["initial_equations"], body["faks"], body["equations"], body["restrictions"])
        return {"status": "Выполнено"}
    except Exception as e:
        logger.info(e)
        return {"status": "Ошибка"}


@app.get("/graphic")
async def get_graphic(request: Request):
    return templates.TemplateResponse(name="graphic.html", context={
        "request": request
    })


@app.get("/diagrams")
async def get_diagrams(request: Request):
    return templates.TemplateResponse(name="diagrams.html", context={
        "request": request
    })
