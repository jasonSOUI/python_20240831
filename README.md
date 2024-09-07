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
`````

```python
# https://depart.femh.org.tw/dietary/3OPD/BMI.htm
def getBMI(height, weight):

    try:
        # 公分轉公尺
        _height = height * Decimal(0.01) 

        # BMI = 體重(公斤) / 身高2(公尺2)
        bmi = weight / (_height ** 2) 
        bmi = bmi.quantize(Decimal('0.1'), rounding=ROUND_HALF_UP)
        
        # 狀態判斷
        status = ""
        if bmi >= 35:               # 重度肥胖：BMI≧35
            status = "重度肥胖"
        elif bmi >= 30:             # 中度肥胖：30≦BMI＜35
            status = "中度肥胖"
        elif bmi >= 27 :            # 輕度肥胖：27≦BMI＜30
             status = "輕度肥胖"  
        elif bmi >= 24:             # 過重：24≦BMI＜27
            status = "過重"        
        elif bmi < 18.5:             # 體重過輕 BMI＜18.5
            status = "體重過輕"         
        else:
            status = "正常範圍"

        return "您的BMI值是{}\n您的體重{}".format(bmi, status)
    except Exception as e:
        traceback.print_exc()
        print("未知錯誤", e)

try:
    height = Decimal(input("請輸入身高(公分)"))
    weight = Decimal(input("請輸入體重(公尺)"))
    print(getBMI(height, weight))
except Exception as e:
    print("請輸入正確的身高、體重，須為數字")
```