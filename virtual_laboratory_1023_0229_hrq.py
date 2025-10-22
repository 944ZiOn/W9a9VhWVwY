# 代码生成时间: 2025-10-23 02:29:32
import numpy as np

"""
Virtual Laboratory
This module simulates a basic virtual laboratory using NumPy for numerical computations.
It is designed to be extensible and maintainable, following best practices in Python programming.
"""

# Define a class for the Virtual Laboratory
class VirtualLaboratory:
    """
    The VirtualLaboratory class simulates basic laboratory operations using NumPy.
    It provides methods to perform calculations and manage data.
    """
    def __init__(self):
        """
        Initializes the VirtualLaboratory with an empty data array.
        """
        self.data = np.array([])

    def add_experiment(self, experiment_data):
        """
        Adds new experiment data to the laboratory.
        
        Parameters:
        experiment_data (np.ndarray): The data from the experiment to be added.
        
        Raises:
        ValueError: If the data is not a NumPy array.
        """
        if not isinstance(experiment_data, np.ndarray):
            raise ValueError("Experiment data must be a NumPy array.")
        self.data = np.concatenate((self.data, experiment_data))

    def calculate_mean(self):
        """
        Calculates the mean of the collected data.
        
        Returns:
        float: The mean of the data.
        
        Raises:
        ValueError: If there is no data to calculate the mean.
        """
        if len(self.data) == 0:
            raise ValueError("No data available to calculate the mean.")
        return np.mean(self.data)

    def calculate_variance(self):
        """
        Calculates the variance of the collected data.
        
        Returns:
        float: The variance of the data.
        
        Raises:
        ValueError: If there is no data to calculate the variance.
        """
        if len(self.data) == 0:
            raise ValueError("No data available to calculate the variance.")
        return np.var(self.data)

    def get_data(self):
        """
        Returns the collected data.
        
        Returns:
        np.ndarray: The collected experiment data.
        """
        return self.data

# Example usage
if __name__ == '__main__':
    # Create an instance of the Virtual Laboratory
    lab = VirtualLaboratory()
    
    # Add some sample data
    sample_data = np.array([1, 2, 3, 4, 5])
    lab.add_experiment(sample_data)
    
    # Calculate and print the mean and variance
    try:
        mean = lab.calculate_mean()
        variance = lab.calculate_variance()
        print(f"Mean: {mean}, Variance: {variance}")
    except ValueError as e:
        print(e)