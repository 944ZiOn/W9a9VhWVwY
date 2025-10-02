# 代码生成时间: 2025-10-03 01:57:17
import yaml
def load_yaml_config(file_path: str) -> dict:    """
    Load YAML configuration from file.
    
    Args:
        file_path (str): The path to the YAML file.
    
    Returns:
        dict: The configuration data as a dictionary.
    
    Raises:
        FileNotFoundError: If the file does not exist.
        yaml.YAMLError: If there is an error in parsing the YAML file.
    """    try:        # Attempt to open and load the YAML file        with open(file_path, 'r') as file:            config = yaml.safe_load(file)    except FileNotFoundError:        raise FileNotFoundError(f"The file {file_path} does not exist.")    except yaml.YAMLError as e:        raise yaml.YAMLError(f"Error parsing YAML file: {e}")    return config
def main():    # Example usage of the YAML loader    # Replace 'config.yaml' with the path to your YAML configuration file    try:        config = load_yaml_config('config.yaml')        print("Configuration loaded successfully:")        print(config)    except Exception as e:        print(f"An error occurred: {e}")if __name__ == "__main__":    main()