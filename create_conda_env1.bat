@echo off
chcp 65001
set ENV_NAME=venv1

rem 檢查環境是否存在
conda env list | findstr /C:"%ENV_NAME%" >nul
if %errorlevel% neq 0 (
    echo 環境 %ENV_NAME% 不存在，正在創建...
    conda create --name %ENV_NAME% python=3.11 --yes
) else (
    echo 環境 %ENV_NAME% 已存在。
)

rem 進入虛擬環境
conda activate %ENV_NAME%

