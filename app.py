"""
极简 Flask Web 应用 — CI/CD 实验演示
"""
from flask import Flask, render_template_string

app = Flask(__name__)

HTML = """<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>CI/CD 实验 — Flask App v2.0 | 姓名：任湘忆 学号：2440664310</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            min-height: 100vh; display: flex; align-items: center; justify-content: center;
        }
        .card {
            background: #fff; border-radius: 16px; padding: 48px 40px;
            text-align: center;
        }
    </style>
</head>
<body>
    <div class="card">
        <h2>CI/CD部署成功! Flask App v2.0密钥配置修复完成</h2>
        <p>姓名：任湘忆 学号：2440664310 | 服务运行正常</p>
    </div>
</body>
</html>
"""


@app.route("/")
def index():
    import socket, platform, datetime
    return render_template_string(
        HTML,
        python_version=platform.python_version(),
        hostname=socket.gethostname(),
        deploy_time=datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        environment="Production" if app.config.get("ENV") == "production" else "Development",
    )


@app.route("/health")
def health():
    return {"status": "healthy"}, 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80, debug=False)