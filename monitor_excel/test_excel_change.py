#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
测试Excel文件变化监听功能
这个脚本会修改test.xlsx文件来触发监听器的变化检测
"""

import pandas as pd
import time
import random

def test_excel_monitoring():
    """测试Excel监听功能"""
    
    print("🧪 开始测试Excel文件变化监听功能...")
    print("💡 请确保monitor_excel.py正在运行中\n")
    
    # 读取当前数据
    try:
        df = pd.read_excel('test.xlsx')
        print(f"📊 当前Excel文件有 {len(df)} 行, {len(df.columns)} 列")
    except Exception as e:
        print(f"❌ 读取Excel文件失败: {e}")
        return
    
    # 测试1: 添加新行
    print("\n🔬 测试1: 添加新行数据...")
    time.sleep(2)
    
    new_row = ['测试商品', '测试分词', '测试链接', '测试数据'] + [''] * (len(df.columns) - 4)
    df_new = df.copy()
    df_new.loc[len(df_new)] = new_row
    
    df_new.to_excel('test.xlsx', index=False)
    print("✅ 已添加新行，等待监听器检测...")
    time.sleep(3)
    
    # 测试2: 修改现有数据
    print("\n🔬 测试2: 修改现有数据...")
    time.sleep(2)
    
    if len(df_new) > 0:
        # 修改第一行的第一列数据
        df_new.iloc[0, 0] = f"修改的数据_{random.randint(1, 100)}"
        df_new.to_excel('test.xlsx', index=False)
        print("✅ 已修改现有数据，等待监听器检测...")
        time.sleep(3)
    
    # 测试3: 删除行
    print("\n🔬 测试3: 删除最后一行...")
    time.sleep(2)
    
    if len(df_new) > 1:
        df_new = df_new.iloc[:-1]  # 删除最后一行
        df_new.to_excel('test.xlsx', index=False)
        print("✅ 已删除最后一行，等待监听器检测...")
        time.sleep(3)
    
    # 测试4: 添加新列
    print("\n🔬 测试4: 添加新列...")
    time.sleep(2)
    
    df_new['新测试列'] = ['测试值'] * len(df_new)
    df_new.to_excel('test.xlsx', index=False)
    print("✅ 已添加新列，等待监听器检测...")
    time.sleep(3)
    
    # 恢复原始数据
    print("\n🔄 恢复原始数据...")
    time.sleep(2)
    df.to_excel('test.xlsx', index=False)
    print("✅ 已恢复原始数据")
    
    print("\n🎉 测试完成！请查看监听器的输出结果")

if __name__ == "__main__":
    test_excel_monitoring() 