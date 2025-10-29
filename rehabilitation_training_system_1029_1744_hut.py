# 代码生成时间: 2025-10-29 17:44:41
import numpy as np

"""
康复训练系统：
这个系统使用NUMPY库来处理和存储康复训练相关的数据。
系统包含以下功能：
- 录入训练数据
- 计算训练结果的平均值、最大值和最小值
- 显示训练统计信息
- 错误处理确保数据的准确性和完整性
"""

class RehabilitationTrainingSystem:
    def __init__(self):
        """初始化康复训练系统"""
        self.training_data = []

    def enter_training_data(self, data):
        """录入训练数据
        
        参数：
        data (list): 训练数据列表
        """
        if not isinstance(data, list):
            raise ValueError("数据必须是列表类型")
        for item in data:
            if not isinstance(item, (int, float)):
                raise ValueError("数据项必须是整数或浮点数")
        self.training_data.extend(data)

    def calculate_statistics(self):
        """计算训练结果的统计信息
        
        返回：
        dict: 包含平均值、最大值和最小值的字典
        """
        if not self.training_data:
            raise ValueError("训练数据为空，无法计算统计信息")
        mean_value = np.mean(self.training_data)
        max_value = np.max(self.training_data)
        min_value = np.min(self.training_data)
        return {'mean': mean_value, 'max': max_value, 'min': min_value}

    def display_statistics(self):
        """显示训练统计信息"""
        statistics = self.calculate_statistics()
        print("训练统计信息：")
        print(f"平均值: {statistics['mean']:.2f}")
        print(f"最大值: {statistics['max']}")
        print(f"最小值: {statistics['min']}")

# 示例用法
if __name__ == '__main__':
    rehab_system = RehabilitationTrainingSystem()
    # 录入训练数据
    try:
        rehab_system.enter_training_data([1, 2, 3, 4, 5])
    except ValueError as e:
        print(f"错误：{e}")
    # 显示训练统计信息
    try:
        rehab_system.display_statistics()
    except ValueError as e:
        print(f"错误：{e}")
