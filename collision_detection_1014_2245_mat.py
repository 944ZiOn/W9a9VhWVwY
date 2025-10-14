# 代码生成时间: 2025-10-14 22:45:52
import numpy as np

# 定义一个类，用于表示几何形状
class Shape:
    def __init__(self, vertices):
        """
        Shape类的构造函数。
        :param vertices: 形状的顶点列表。
        """
        self.vertices = np.array(vertices)

    def get_vertices(self):
        """
        返回形状的所有顶点。
        :return: 一个包含所有顶点的numpy数组。
        """
        return self.vertices

# 定义一个类，用于表示碰撞检测系统
class CollisionDetectionSystem:
    def __init__(self):
        """
        CollisionDetectionSystem类的构造函数。
        """
        self.shapes = []

    def add_shape(self, shape):
        """
        添加一个新的形状到系统中。
        :param shape: 要添加的形状对象。
        """
        if not isinstance(shape, Shape):
            raise TypeError("添加的对象必须是Shape类的实例")
        self.shapes.append(shape)

    def remove_shape(self, shape):
        """
        从系统中移除一个形状。
        :param shape: 要移除的形状对象。
        """
        try:
            self.shapes.remove(shape)
        except ValueError:
            print("未找到该形状，无法移除")

    def check_collision(self):
        "