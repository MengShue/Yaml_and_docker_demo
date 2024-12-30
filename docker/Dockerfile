# 使用 Python 作為基底映像檔
FROM python:3.10-slim

LABEL maintainer="alan.sung"

LABEL email="meng.s.song@gmail.com"

# 設定工作目錄
WORKDIR /app

# 複製程式碼
COPY ../src /app/src
COPY ../requirements.txt /app/

# 安裝必要套件
RUN pip install -r requirements.txt

# 將 lookup-cli 安裝為可執行指令
RUN chmod +x /app/src/lookup-cli && \
    ln -s /app/src/lookup-cli /usr/local/bin/lookup-cli

# 設定 YAML 配置文件環境變數
ENV CONFIG_PATH=/app/config/data.yaml

# 設定工作目錄為 src 資料夾
WORKDIR /app/src

# 預設執行參數
CMD ["tail","-f","/dev/null"]