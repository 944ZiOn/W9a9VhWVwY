# 代码生成时间: 2025-10-31 08:58:14
import numpy as np

"""
Data Sharding Module
# TODO: 优化性能

This module implements a simple data sharding strategy where data is divided
into shards based on a predefined number of shards.
"""

def shard_data(data, num_shards):
# 增强安全性
    """
    Shard the given data into a specified number of shards.
    
    Parameters:
    data (np.ndarray): The data array to be sharded.
    num_shards (int): The number of shards to divide the data into.
    
    Returns:
# FIXME: 处理边界情况
    list: A list of sharded data arrays.
# 增强安全性
    
    Raises:
    ValueError: If num_shards is less than 1.
    TypeError: If data is not a numpy array.
    """
    if not isinstance(data, np.ndarray):
        raise TypeError("Data must be a numpy array.")
    if num_shards < 1:
        raise ValueError("Number of shards must be at least 1.")
# NOTE: 重要实现细节
    
    # Calculate the size of each shard
    shard_size = len(data) // num_shards
    shards = []
    
    # Shard the data
# 改进用户体验
    for i in range(num_shards):
        start_idx = i * shard_size
        # Ensure the last shard gets all remaining elements
        end_idx = (i + 1) * shard_size if i < num_shards - 1 else len(data)
        shard = data[start_idx:end_idx]
        shards.append(shard)
    
    return shards

# Example usage
# TODO: 优化性能
if __name__ == '__main__':
    # Create a sample numpy array
    data_array = np.arange(100)
    
    # Shard the data into 4 shards
    num_shards = 4
    try:
        sharded_data = shard_data(data_array, num_shards)
        for i, shard in enumerate(sharded_data):
            print(f"Shard {i+1}: {shard}")
    except (ValueError, TypeError) as e:
        print(f"Error: {e}")