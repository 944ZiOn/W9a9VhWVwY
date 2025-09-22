# 代码生成时间: 2025-09-23 00:52:37
import numpy as np

"""
A simple user permission management system using Python and NumPy.
This program allows for adding, removing, and checking user permissions.
"""

class UserPermissionManager:
    """
    A class to manage user permissions.
    """
    def __init__(self):
        # Initialize a dictionary to store user permissions
        self.permissions = {}

    def add_user(self, username):
        """
        Add a new user to the system.
        :param username: The username of the user to add.
        """
        if username in self.permissions:
            raise ValueError("User already exists.")
        self.permissions[username] = set()

    def remove_user(self, username):
        """
        Remove a user from the system.
        :param username: The username of the user to remove.
        """
        if username not in self.permissions:
            raise ValueError("User does not exist.")
        del self.permissions[username]

    def add_permission(self, username, permission):
        """
        Add a permission to a user.
        :param username: The username of the user to grant permission to.
        :param permission: The permission to grant.
        """
        if username not in self.permissions:
            raise ValueError("User does not exist.")
        self.permissions[username].add(permission)

    def remove_permission(self, username, permission):
        """
        Remove a permission from a user.
        :param username: The username of the user to revoke permission from.
        :param permission: The permission to revoke.
        """
        if username not in self.permissions:
            raise ValueError("User does not exist.")
        if permission in self.permissions[username]:
            self.permissions[username].remove(permission)
        else:
            raise ValueError("Permission does not exist for the user.")

    def check_permission(self, username, permission):
        """
        Check if a user has a specific permission.
        :param username: The username of the user to check.
        :param permission: The permission to check for.
        :return: True if the user has the permission, False otherwise.
        """
        if username not in self.permissions:
            raise ValueError("User does not exist.")
        return permission in self.permissions[username]

    def list_permissions(self, username):
        """
        List all permissions for a user.
        :param username: The username of the user to list permissions for.
        :return: A list of permissions.
        """
        if username not in self.permissions:
            raise ValueError("User does not exist.")
        return list(self.permissions[username])

# Example usage:
if __name__ == '__main__':
    manager = UserPermissionManager()
    try:
        manager.add_user("alice")
        manager.add_permission("alice", "read")
        manager.add_permission("alice", "write")
        print(manager.check_permission("alice", "read"))  # Should print True
        print(manager.list_permissions("alice"))  # Should print ['read', 'write']
        manager.remove_permission("alice", "read")
        print(manager.check_permission("alice", "read"))  # Should print False
    except ValueError as e:
        print(f"Error: {e}")