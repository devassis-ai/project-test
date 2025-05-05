from fastapi import FastAPI, Request
import subprocess

app = FastAPI()

# 실제 Git 저장소 경로
REPO_PATH = r"C:/Users/js11w/Documents/GitHub/project-test"

@app.post("/github-webhook")
async def github_webhook(request: Request):
    payload = await request.json()

    if 'ref' in payload:
        print("🔄 GitHub Push 감지됨: 자동 pull 시작")

        try:
            # 경로 하드코딩 대신 변수 사용
            subprocess.run(["git", "-C", REPO_PATH, "pull"], check=True)
            print("✅ pull 완료")
        except subprocess.CalledProcessError as e:
            print("❌ pull 실패:", e)

    return {"status": "ok"}
