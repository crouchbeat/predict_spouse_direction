import sxtwl
from datetime import datetime

def is_valid_date(year, month, day):
    """验证日期是否有效"""
    try:
        datetime(year, month, day)
        return True
    except ValueError:
        return False

def get_spouse_direction(year, month, day):
    # 验证输入日期的有效性
    if not is_valid_date(year, month, day):
        raise ValueError(f"无效的日期：{year}年{month}月{day}日，请输入有效的日期")
    print(f"DEBUG: 输入参数 - 年: {year}, 月: {month}, 日: {day}")

    lunar = sxtwl.Lunar()
    day = lunar.getDayBySolar(year, month, day)
    dizhi = ['子', '丑', '寅', '卯', '辰', '巳', '午', '未', '申', '酉', '戌', '亥']
    lunar_month_dz = dizhi[day.Lmonth2.dz]  
    print(f"DEBUG: 月地支索引: {day.Lmonth2.dz}, 对应地支: {lunar_month_dz}")

    direction_map = {
        '子': '正南或正北',
        '午': '正南或正北',
        '卯': '正东或正西',
        '酉': '正东或正西',
        '未': '西南或东北',
        '申': '西南或东北',
        '寅': '西南或东北',
        '丑': '西南或东北',
        '辰': '东南或西北',
        '巳': '东南或西北',
        '戌': '东南或西北',
        '亥': '东南或西北'
    }

    start_index = dizhi.index(lunar_month_dz)  # 月对应的地支作为起始点

    # 使用真正的农历日期减一
    lunar_day_offset = day.Ldi 
    print(f"DEBUG: 农历日期Ldi 偏移量: {lunar_day_offset}")
    
    end_index = (start_index + lunar_day_offset) % 12  # 顺行数至所生的日子
    dizhi_result = dizhi[end_index]

    return direction_map[dizhi_result]

def main():
    # 测试有效日期
    try:
        year = 2024
        month = 2
        day = 15  # 有效日期
        direction = get_spouse_direction(year, month, day)
        print(f"配偶所在的方位为：{direction}")
    except ValueError as e:
        print(f"错误：{e}")

    # 测试无效日期（2月31日不存在）
    try:
        year = 2024
        month = 2
        day = 31  # 无效日期
        direction = get_spouse_direction(year, month, day)
        print(f"配偶所在的方位为：{direction}")
    except ValueError as e:
        print(f"错误：{e}")

if __name__ == "__main__":
    main()
