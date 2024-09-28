## 20240831 python pico lesson 01 
+ [20240831 Python課程錄影](https://www.youtube.com/watch?v=Xr1jz5rSk7M)
+ 課程Google meet : https://meet.google.com/wuv-njsa-ejb
+ 課程Github : https://github.com/roberthsu2003/pico_W
+ picoWH (Wifi版本)
+ [colab](https://colab.research.google.com/) (雲端python開發環境)
+ 查看[Codespaces](https://github.com/codespaces)(平時記得要確認有關閉) : 
+ 安裝Jupyter 

## 20240907 python pico lesson 02 
+ 安裝[github](https://desktop.github.com/download/)
+ 安裝[vscode](https://code.visualstudio.com/)
+ 安裝[git](https://git-scm.com/download/win)
+ 安裝[Miniconda](https://docs.anaconda.com/miniconda/index.html)
+ [conde環境設定](https://github.com/roberthsu2003/python/tree/master/mini_conda)
+ [git設定](https://github.com/roberthsu2003/python/tree/master/vscode%E8%A8%AD%E5%AE%9A)

```bash
# 查看環境
conda env list
# 建立venv1虛擬環境，python版本3.11
conda create --name venv1 python=3.11
# 進入虛擬環境
conda activate venv1
# 離開虛擬環境
conda deactivate    
# 刪除虛擬環境
conda env remove --name venv1
# conda更新 
conda update conda

# git設定
git config --global user.name "jason"
git config --global user.email "jason@soui.com.tw"
git config --global pull.rebase false
git config --global credential.name "jason@soui.com.tw"

# wifi
wifi : A590301 / A590301AA
server : piRobert0301.local
`````

### 20240914 python pico lesson 03
+ while、for迴圈
+ function 參數、回傳值(tuple、list、dict)
+ import package、module
+ [https://pypi.org/](https://pypi.org/)


### 20240921 python pico lesson 04
+ 安裝到實體pico(按著白色按鈕插入USB後放開、會讀取到RPI-RP2磁碟區，將RPI_PICO_W-20240602-v1.23.0.uf2複製到RPI-RP2磁碟區) [Raspberry Pi Pico W](https://www.raspberrypi.com/documentation/microcontrollers/micropython.html)
+ 安裝[Thonny](https://thonny.org/)

