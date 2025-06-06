# Excel文件变化监听器使用说明

## 功能介绍

这个监听器可以实时监听 `test.xlsx` 文件的变化，当文件发生变更时会打印出具体的变化内容。

## 文件说明

1. **`monitor_excel.py`** - 完整版监听器
   - 功能最全面，可以检测详细的数据变化
   - 显示新增/删除的行和列
   - 显示数据内容的具体变化

2. **`simple_monitor.py`** - 简化版监听器
   - 更容易理解和调试
   - 专注于基本的变化检测

3. **`test_excel_change.py`** - 测试脚本
   - 自动修改Excel文件来测试监听功能

## 安装依赖

```bash
pip3 install watchdog pandas openpyxl
```

## 使用方法

### 方法1：使用完整版监听器

```bash
# 启动监听器
python3 monitor_excel.py

# 在另一个终端窗口运行测试
python3 test_excel_change.py
```

### 方法2：使用简化版监听器

```bash
# 启动简化版监听器
python3 simple_monitor.py

# 手动修改test.xlsx文件，或者运行测试脚本
```

## 监听器功能特点

### 🔍 检测的变化类型：

- ➕ **新增行数据** - 检测到新增的行，并显示新增内容
- ➖ **删除行数据** - 检测到删除的行数量
- ➕ **新增列** - 检测到新增的列名
- ➖ **删除列** - 检测到删除的列名
- 🔄 **修改数据** - 检测到具体单元格的数据变化
- 📐 **数据形状变化** - 显示行列数的变化

### 📊 显示信息：

- 文件变化时间戳
- 数据维度变化 (行数 x 列数)
- 具体的变化内容
- 新增数据的预览

## 示例输出

```
✅ 开始监听文件: test.xlsx
📊 初始数据加载完成，共 81 行，13 列

🔔 检测到文件变化: 2024-01-20 17:45:23
📝 检测到以下变化:
   📐 数据形状变化: (81, 13) → (82, 13)
   ➕ 新增 1 行数据
   新增的行数据:
   第82行: ['测试商品', '测试分词', '测试链接', '测试数据', ...]

🔔 检测到文件变化: 2024-01-20 17:45:26
📝 检测到以下变化:
   🔄 第1行 '序号' 列: 原值 → 修改的数据_42
```

## 停止监听

按 `Ctrl+C` 停止监听器

## 注意事项

1. 确保 `test.xlsx` 文件存在于当前目录
2. 监听器会在文件被其他程序（如Excel）修改时触发
3. 监听器有0.5秒的延迟以确保文件写入完成
4. 如果Excel文件被锁定（如正在被Excel打开），可能无法正确读取变化

## 技术实现

- 使用 `watchdog` 库监听文件系统事件
- 使用 `pandas` 读取和比较Excel数据
- 使用 `openpyxl` 引擎处理Excel文件格式 