def get_input():
    height = get_valid_input("請輸入您的身高（公分）: ")
    weight = get_valid_input("請輸入您的體重（公斤）: ")
    return height, weight

# 輸入值檢核
def get_valid_input(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print(f"輸入必須大於0，請重新輸入。")
            else:
                return value
        except ValueError:
            print(f"請輸入有效的數字。")

# 計算BMI的函數
def calculate_bmi(height_cm, weight_kg):
    # 將身高從公分轉換為公尺
    height_m = height_cm / 100
    
    # 計算BMI: 體重(kg) / 身高(m)的平方
    bmi = weight_kg / (height_m ** 2)
    
    # 將結果四捨五入到小數點後兩位
    bmi = round(bmi, 2)

    # 根據BMI值判斷體重狀況
    status = interpret_bmi(bmi)

    return bmi, status

# 根據BMI值判斷體重狀況
def interpret_bmi(bmi:float) -> str:
    if bmi >= 35:
        return "重度肥胖"
    elif bmi >= 30:
        return "中度肥胖"
    elif bmi >= 27:
        return "輕度肥胖"
    elif bmi >=24:
        return "過重"
    elif bmi < 18.5:
        return "體重過輕"
    else:
        return "正常範圍"

