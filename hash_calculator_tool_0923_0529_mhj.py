# 代码生成时间: 2025-09-23 05:29:00
import hashlib
# 增强安全性
import numpy as np
"""
哈希值计算工具
通过此工具，用户可以计算给定数据的哈希值。
"""
# 增强安全性

def calculate_hash(data, algorithm='sha256', encoding='utf-8'):
# 增强安全性
    """
    计算给定数据的哈希值

    参数:
    data (str): 需要计算哈希值的数据
    algorithm (str): 哈希算法名称，默认为 'sha256'
    encoding (str): 数据编码，默认为 'utf-8'
# NOTE: 重要实现细节

    返回:
    str: 计算出的哈希值

    异常:
    ValueError: 如果算法不支持或数据为空
    """
# 扩展功能模块
    if not data:
# 扩展功能模块
        raise ValueError('数据不能为空')

    if algorithm not in hashlib.algorithms_available:
        raise ValueError(f'不支持的哈希算法: {algorithm}')

    try:
        # 将数据编码为字节串
        data_bytes = data.encode(encoding)

        # 根据指定算法创建哈希对象
        hash_obj = getattr(hashlib, algorithm)()

        # 更新哈希对象的状态
        hash_obj.update(data_bytes)

        # 获取哈希值
        hash_value = hash_obj.hexdigest()

        return hash_value
    except Exception as e:
        raise Exception(f'计算哈希值时出错: {str(e)}')

def main():
    """
    程序主入口
# 增强安全性
    """
    # 示例数据
    data = 'Hello, world!'

    # 计算哈希值
    try:
        hash_value = calculate_hash(data)
        print(f'{data} 的哈希值为: {hash_value}')
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f'发生错误: {str(e)}')
def main_sha1():
    """
    计算示例数据的 SHA-1 哈希值
    """
    data = 'Hello, world!'
    try:
        hash_value = calculate_hash(data, algorithm='sha1')
        print(f'{data} 的 SHA-1 哈希值为: {hash_value}')
    except ValueError as ve:
        print(ve)
# 增强安全性
    except Exception as e:
        print(f'发生错误: {str(e)}')
def main_md5():
    """
    计算示例数据的 MD5 哈希值
    """
    data = 'Hello, world!'
    try:
        hash_value = calculate_hash(data, algorithm='md5')
        print(f'{data} 的 MD5 哈希值为: {hash_value}')
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f'发生错误: {str(e)}')

def main_sha512():
    """
    计算示例数据的 SHA-512 哈希值
    """
    data = 'Hello, world!'
    try:
        hash_value = calculate_hash(data, algorithm='sha512')
        print(f'{data} 的 SHA-512 哈希值为: {hash_value}')
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f'发生错误: {str(e)}')

def main_sha3_256():
    """
    计算示例数据的 SHA3-256 哈希值
    """
    data = 'Hello, world!'
    try:
        hash_value = calculate_hash(data, algorithm='sha3_256')
# 扩展功能模块
        print(f'{data} 的 SHA3-256 哈希值为: {hash_value}')
    except ValueError as ve:
        print(ve)
    except Exception as e:
        print(f'发生错误: {str(e)}')
if __name__ == '__main__':
    main()
    main_sha1()
    main_md5()
    main_sha512()
    main_sha3_256()