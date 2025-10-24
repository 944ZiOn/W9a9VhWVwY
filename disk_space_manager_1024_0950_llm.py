# 代码生成时间: 2025-10-24 09:50:36
import os
import shutil
import numpy as np

"""
A disk space management tool using Python and NumPy.
This tool provides functionality to check disk space,
delete unnecessary files, and manage disk space efficiently.
"""

class DiskSpaceManager:
    """Class to manage disk space."""

    def __init__(self, root_path="."):
        """Initialize the DiskSpaceManager with a root path."""
        self.root_path = root_path

    def check_disk_space(self):
        """Check the total and used disk space."""
        total, used, free = shutil.disk_usage(self.root_path)
        return {
            "total": total,
            "used": used,
            "free": free,
        }

    def delete_large_files(self, min_size_mb):
        """Delete files larger than a specified size (in MB)."""
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                file_path = os.path.join(root, file)
                if os.path.getsize(file_path) > min_size_mb * 1024 * 1024:
                    try:
                        os.remove(file_path)
                        print(f"Deleted large file: {file_path}")
                    except Exception as e:
                        print(f"Failed to delete file: {file_path}. Error: {e}")

    def analyze_file_sizes(self):
        """Analyze file sizes and return a histogram."""
        file_sizes = []
        for root, dirs, files in os.walk(self.root_path):
            for file in files:
                file_path = os.path.join(root, file)
                file_sizes.append(os.path.getsize(file_path))

        # Use NumPy to create a histogram
        bins = np.histogram_bin_edges(file_sizes, bins="auto")
        hist, _ = np.histogram(file_sizes, bins=bins)
        return hist

    def print_disk_space_info(self):
        """Print detailed disk space information."""
        disk_info = self.check_disk_space()
        print(f"Total disk space: {disk_info['total'] / (1024 ** 3):.2f} GB")
        print(f"Used disk space: {disk_info['used'] / (1024 ** 3):.2f} GB")
        print(f"Free disk space: {disk_info['free'] / (1024 ** 3):.2f} GB")

# Example usage
if __name__ == "__main__":
    manager = DiskSpaceManager()
    print(manager.check_disk_space())
    manager.delete_large_files(100)  # Delete files larger than 100 MB
    hist = manager.analyze_file_sizes()
    print(hist)
    manager.print_disk_space_info()