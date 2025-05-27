#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Excel文件变化监听器
监听test.xlsx文件，当文件发生变化时打印出具体的变化内容
"""

import os
import time
import pandas as pd
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from datetime import datetime
import json

class ExcelFileHandler(FileSystemEventHandler):
    """Excel文件变化处理器"""
    
    def __init__(self, excel_file_path):
        self.excel_file_path = excel_file_path
        self.previous_data = None
        self.load_initial_data()
        
    def load_initial_data(self):
        """加载初始数据"""
        if os.path.exists(self.excel_file_path):
            try:
                self.previous_data = pd.read_excel(self.excel_file_path)
                print(f"✅ 开始监听文件: {self.excel_file_path}")
                print(f"📊 初始数据加载完成，共 {len(self.previous_data)} 行，{len(self.previous_data.columns)} 列")
                self.print_data_info(self.previous_data, "初始数据")
            except Exception as e:
                print(f"❌ 加载初始数据失败: {e}")
                self.previous_data = None
        else:
            print(f"⚠️  文件不存在: {self.excel_file_path}")
            self.previous_data = None
    
    def print_data_info(self, data, title):
        """打印数据信息"""
        print(f"\n--- {title} ---")
        print(f"📏 数据维度: {data.shape}")
        if not data.empty:
            print(f"📋 列名: {list(data.columns)}")
            print(f"🔢 前5行数据:")
            print(data.head().to_string(index=True))
        print("-" * 50)
    
    def compare_dataframes(self, old_df, new_df):
        """比较两个DataFrame的差异"""
        changes = []
        
        # 如果旧数据为空
        if old_df is None or old_df.empty:
            return [f"➕ 新增了全部数据 ({len(new_df)} 行)"]
        
        # 如果新数据为空
        if new_df.empty:
            return ["🗑️  数据被清空"]
        
        # 比较形状变化
        if old_df.shape != new_df.shape:
            changes.append(f"📐 数据形状变化: {old_df.shape} → {new_df.shape}")
        
        # 比较列名变化
        old_cols = set(old_df.columns)
        new_cols = set(new_df.columns)
        
        if old_cols != new_cols:
            added_cols = new_cols - old_cols
            removed_cols = old_cols - new_cols
            
            if added_cols:
                changes.append(f"➕ 新增列: {list(added_cols)}")
            if removed_cols:
                changes.append(f"➖ 删除列: {list(removed_cols)}")
        
        # 对于相同的列，比较数据变化
        common_cols = old_cols & new_cols
        if common_cols:
            try:
                # 重新索引以便比较
                old_common = old_df[list(common_cols)].reset_index(drop=True)
                new_common = new_df[list(common_cols)].reset_index(drop=True)
                
                # 比较行数变化
                old_rows = len(old_common)
                new_rows = len(new_common)
                
                if old_rows != new_rows:
                    if new_rows > old_rows:
                        changes.append(f"➕ 新增 {new_rows - old_rows} 行数据")
                        # 显示新增的行
                        if new_rows - old_rows <= 5:  # 只显示前5行新增数据
                            new_rows_data = new_df.iloc[old_rows:].to_string(index=True)
                            changes.append(f"新增的行数据:\n{new_rows_data}")
                    else:
                        changes.append(f"➖ 删除 {old_rows - new_rows} 行数据")
                
                # 比较现有行的变化
                min_rows = min(old_rows, new_rows)
                for i in range(min_rows):
                    for col in common_cols:
                        old_val = old_common.iloc[i][col]
                        new_val = new_common.iloc[i][col]
                        
                        # 处理NaN值的比较
                        if pd.isna(old_val) and pd.isna(new_val):
                            continue
                        elif pd.isna(old_val) or pd.isna(new_val) or old_val != new_val:
                            changes.append(f"🔄 第{i+1}行 '{col}' 列: {old_val} → {new_val}")
                            
            except Exception as e:
                changes.append(f"❌ 比较数据时出错: {e}")
        
        return changes if changes else ["✅ 文件已更新，但数据内容无变化"]
    
    def on_modified(self, event):
        """文件被修改时的回调"""
        if event.is_directory:
            return
            
        # 只处理我们关心的Excel文件
        if event.src_path.endswith(os.path.basename(self.excel_file_path)):
            print(f"\n🔔 检测到文件变化: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
            
            # 短暂延迟，确保文件写入完成
            time.sleep(0.5)
            
            try:
                # 读取新数据
                current_data = pd.read_excel(self.excel_file_path)
                
                # 比较变化
                changes = self.compare_dataframes(self.previous_data, current_data)
                
                # 打印变化
                print("📝 检测到以下变化:")
                for change in changes:
                    print(f"   {change}")
                
                # 如果有实际数据变化，显示当前数据概览
                if len(changes) > 1 or not changes[0].startswith("✅"):
                    self.print_data_info(current_data, "当前数据")
                
                # 更新缓存的数据
                self.previous_data = current_data.copy()
                
            except Exception as e:
                print(f"❌ 处理文件变化时出错: {e}")

def main():
    """主函数"""
    excel_file = "test.xlsx"
    
    # 检查文件是否存在
    if not os.path.exists(excel_file):
        print(f"❌ 文件不存在: {excel_file}")
        print("请确保 test.xlsx 文件在当前目录中")
        return
    
    # 创建事件处理器
    event_handler = ExcelFileHandler(excel_file)
    
    # 创建观察者
    observer = Observer()
    observer.schedule(event_handler, path='.', recursive=False)
    
    # 启动监听
    observer.start()
    print(f"🚀 开始监听 {excel_file} 的变化...")
    print("💡 提示: 按 Ctrl+C 停止监听\n")
    
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n🛑 停止监听...")
        observer.stop()
    
    observer.join()
    print("✅ 监听已停止")

if __name__ == "__main__":
    main()
