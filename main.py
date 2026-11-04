from fastapi import FastAPI
from fastapi.responses import HTMLResponse, JSONResponse, Response

app = FastAPI()

HTML_PAGE = """<!DOCTYPE html><html lang="fr"><head><meta charset="UTF-8"><meta name="viewport" content="width=device-width, initial-scale=1.0"><title>Dieng Predict V18</title><style>body{background:#0a0e13;color:#fff;font-family:Arial;padding:10px}.header{background:linear-gradient(90deg,#00ff88,#00aaff);padding:14px;border-radius:12px;text-align:center;color:#000;font-weight:bold}.tabs{display:flex;gap:6px;margin:12px 0;overflow-x:auto}.tab{padding:10px 14px;border-radius:20px;background:#1e222b;color:#888;border:1px solid #333;cursor:pointer;white-space:nowrap}.tab.active{background:#00ff88;color:#000;font-weight:bold}.card{background:#151a22;border:1px solid #2a2e38;border-radius:14px;padding:14px
