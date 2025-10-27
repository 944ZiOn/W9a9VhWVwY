# 代码生成时间: 2025-10-28 00:10:11
import numpy as np

"""
Digital Identity Verification Program
This program simulates a digital identity verification process
using Python and NumPy. It checks if a provided user input
matches the stored identity information.
"""

# Constants
IDENTITY_INFO = {
    "user_id": 1234,
    "password": 5678
}

def verify_identity(user_id, password):
    """
    Verifies the provided user ID and password against the stored identity information.

    Parameters:
    user_id (int): The user's ID to verify.
    password (int): The user's password to verify.

    Returns:
    bool: True if the identity is verified, False otherwise.
    
    Raises:
    ValueError: If any of the input values are not integers.
    """
    if not isinstance(user_id, int) or not isinstance(password, int):
        raise ValueError("Both user ID and password must be integers.")

    try:
        # Check if the provided credentials match the stored identity information
        return (user_id, password) == tuple(IDENTITY_INFO.values())
    except TypeError:
        raise ValueError("The identity information is corrupted. Please check the stored values.")

def main():
    """
    Main function to simulate the digital identity verification process.
    """
    try:
        # Collect user input for user ID and password
        user_id = int(input("Enter your user ID: "))
        password = int(input("Enter your password: "))

        # Verify the identity
        if verify_identity(user_id, password):
            print("Identity verified successfully.")
        else:
            print("Identity verification failed.")
    except ValueError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()