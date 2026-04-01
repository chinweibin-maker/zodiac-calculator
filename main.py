# 简单的生肖与星座计算器 / Simple Zodiac & Horoscope Calculator
#1APR2026
def get_zodiac(year):
    """根据年份计算生肖"""
    zodiacs = ["猴 (Monkey)", "鸡 (Rooster)", "狗 (Dog)", "猪 (Pig)", 
               "鼠 (Rat)", "牛 (Ox)", "虎 (Tiger)", "兔 (Rabbit)", 
               "龙 (Dragon)", "蛇 (Snake)", "马 (Horse)", "羊 (Goat)"]
    return zodiacs[year % 12]

def get_horoscope(month, day):
    """根据月日计算星座"""
    if (month == 3 and day >= 21) or (month == 4 and day <= 19):
        return "白羊座 (Aries)"
    elif (month == 4 and day >= 20) or (month == 5 and day <= 20):
        return "金牛座 (Taurus)"
    elif (month == 5 and day >= 21) or (month == 6 and day <= 21):
        return "双子座 (Gemini)"
    elif (month == 6 and day >= 22) or (month == 7 and day <= 22):
        return "巨蟹座 (Cancer)"
    elif (month == 7 and day >= 23) or (month == 8 and day <= 22):
        return "狮子座 (Leo)"
    elif (month == 8 and day >= 23) or (month == 9 and day <= 22):
        return "处女座 (Virgo)"
    elif (month == 9 and day >= 23) or (month == 10 and day <= 23):
        return "天秤座 (Libra)"
    elif (month == 10 and day >= 24) or (month == 11 and day <= 22):
        return "天蝎座 (Scorpio)"
    elif (month == 11 and day >= 23) or (month == 12 and day <= 21):
        return "射手座 (Sagittarius)"
    elif (month == 12 and day >= 22) or (month == 1 and day <= 19):
        return "摩羯座 (Capricorn)"
    elif (month == 1 and day >= 20) or (month == 2 and day <= 18):
        return "水瓶座 (Aquarius)"
    else:
        return "双鱼座 (Pisces)"

# --- 测试运行 ---
print("--- 欢迎使用个人星盘工具 / Welcome to Personal Astro Tool ---")
birth_year = int(input("请输入出生年份 (Enter Birth Year): "))
birth_month = int(input("请输入出生月份 (Enter Birth Month 1-12): "))
birth_day = int(input("请输入出生日期 (Enter Birth Day): "))

print(f"\n你的生肖是 (Your Zodiac): {get_zodiac(birth_year)}")
print(f"你的星座是 (Your Horoscope): {get_horoscope(birth_month, birth_day)}")
