from fastapi import FastAPI, Request
import subprocess
import os

app = FastAPI()

# 📁 Git 저장소 경로 설정 (반드시 로컬 경로로 수정!)
REPO_PATH = r"C:\\Users\\js11w\\Documents\\GitHub\\project-test"  # ← 여기를 수정하세요

@app.post("/github-webhook")
async def github_webhook(request: Request):
    payload = await request.json()
    
    # GitHub Push 이벤트 확인
    if 'ref' in payload:
        print("🔄 GitHub Push 감지됨: 자동 pull 시작")
        
        # git pull 실행
        try:
            subprocess.run(["git", "-C", REPO_PATH, "pull"], check=True)
            print("✅ pull 완료")
        except subprocess.CalledProcessError as e:
            print("❌ pull 실패:", e)
    
    return {"status": "ok"}
