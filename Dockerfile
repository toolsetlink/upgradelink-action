# 使用Python基础镜像
FROM python:3.9-slim

# 设置工作目录
WORKDIR /action

# 复制依赖文件并安装
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 复制主脚本
COPY main.py .

# 设置入口点
ENTRYPOINT ["python", "/action/main.py"]