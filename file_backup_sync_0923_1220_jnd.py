# 代码生成时间: 2025-09-23 12:20:33
import os
import shutil
import numpy as np
from datetime import datetime

class FileBackupSync:
    """文件备份和同步工具"""

    def __init__(self, source_dir, backup_dir):
        """初始化函数"""
        self.source_dir = source_dir
        self.backup_dir = backup_dir

    def create_backup_directory(self):
        """创建备份目录"""
        try:
            os.makedirs(self.backup_dir, exist_ok=True)
            print(f"备份目录 {self.backup_dir} 创建成功")
        except Exception as e:
            print(f"创建备份目录失败: {e}")

    def get_files(self):
        """获取源目录下所有文件"""
        try:
            return [os.path.join(self.source_dir, f) for f in os.listdir(self.source_dir) if os.path.isfile(os.path.join(self.source_dir, f))]
        except Exception as e:
            print(f"获取源目录文件失败: {e}")
            return []

    def backup_files(self):
        """备份文件"""
        self.create_backup_directory()
        files = self.get_files()
        for file in files:
            try:
                shutil.copy2(file, self.backup_dir)
                print(f"文件 {file} 备份成功")
            except Exception as e:
                print(f"文件 {file} 备份失败: {e}")

    def sync_files(self):
        """同步文件"""
        self.create_backup_directory()
        source_files = set(os.listdir(self.source_dir))
        backup_files = set(os.listdir(self.backup_dir))
        new_files = source_files - backup_files
        modified_files = {f for f in source_files & backup_files if os.path.getmtime(os.path.join(self.source_dir, f)) > os.path.getmtime(os.path.join(self.backup_dir, f))}
        
        for file in new_files | modified_files:
            try:
                source_file = os.path.join(self.source_dir, file)
                backup_file = os.path.join(self.backup_dir, file)
                shutil.copy2(source_file, backup_file)
                print(f"文件 {file} 同步成功")
            except Exception as e:
                print(f"文件 {file} 同步失败: {e}")

    def run(self):
        """运行备份或同步操作"""
        self.backup_files()
        self.sync_files()

# 示例用法
if __name__ == "__main__":
    source_directory = "/path/to/source"
    backup_directory = "/path/to/backup"
    backup_sync_tool = FileBackupSync(source_directory, backup_directory)
    backup_sync_tool.run()
