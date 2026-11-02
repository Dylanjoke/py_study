# 1. 改造记账本：加一个"删除第 N 条"的功能（提示：读到列表里，删掉，再整体写回）
def delete_entry(entries, index):
    if 0 <= index < len(entries):
        del entries[index]
        print(f"已删除第 {index + 1} 条记录。")
    else:
        print("索引超出范围，无法删除。")

# 2. 在函数里用 try/except 包住文件读取，处理文件不存在的情况
def read_entries_from_file(filename):
    try:
        with open(filename, "r", encoding="utf-8") as f:
            entries = f.readlines()
        return entries
    except FileNotFoundError:
        print("文件不存在。")
        return []
    except Exception as e:
        print(f"读取文件时发生错误: {e}")
        return []

# 3. 试着把数据存成 CSV 格式（用逗号分隔），然后用 Excel 打开看看
def save_entries_to_csv(entries, filename):
    try:
        with open(filename, "w", encoding="utf-8") as f:
            for entry in entries:
                f.write(entry.strip() + "\n")
    except Exception as e:
        print(f"保存文件时发生错误: {e}")