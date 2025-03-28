from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import uvicorn
import os
from dotenv import load_dotenv
from huggingface_hub import login
import sys

# 環境変数の読み込み
load_dotenv(dotenv_path=".env", override=True)
if os.getenv("HF_TOKEN"):
    login(os.getenv("HF_TOKEN"))

# run.pyの関数をインポート
from scripts.text_inspector_tool import TextInspectorTool
from scripts.text_web_browser import (
    ArchiveSearchTool,
    FinderTool,
    FindNextTool,
    PageDownTool,
    PageUpTool,
    SimpleTextBrowser,
    VisitTool,
)
from scripts.visual_qa import visualizer

from smolagents import (
    CodeAgent,
    GoogleSearchTool,
    LiteLLMModel,
    ToolCallingAgent,
)

# run.pyから必要な関数とグローバル変数をインポート
from run import (
    create_agent,
    AUTHORIZED_IMPORTS,
    custom_role_conversions,
    BROWSER_CONFIG,
)


# APIモデルの定義
class ResearchRequest(BaseModel):
    topic: str
    model_id: str = "o1"


class ResearchResponse(BaseModel):
    result: str


# FastAPIアプリケーションの作成
app = FastAPI(
    title="Research API",
    description="リサーチトピックに基づいて情報を提供するAPI",
    version="1.0.0",
)


@app.post("/research", response_model=ResearchResponse)
async def research(request: ResearchRequest):
    try:
        # エージェントの作成
        agent = create_agent(model_id=request.model_id)

        # リサーチの実行
        answer = agent.run(request.topic)

        return ResearchResponse(result=answer)
    except Exception as e:
        raise HTTPException(
            status_code=500, detail=f"リサーチ実行中にエラーが発生しました: {str(e)}"
        )


@app.get("/")
async def root():
    return {
        "message": "Research APIへようこそ。/research エンドポイントにPOSTリクエストを送信してリサーチを実行してください。"
    }


if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
