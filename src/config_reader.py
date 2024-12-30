import yaml
import os


class ConfigReader:
    """YAML 設定檔讀取類別"""

    def __init__(self, file_path: str):
        """
        初始化並讀取 YAML 文件
        :param file_path: YAML 文件路徑
        """
        self.file_path = file_path
        self.data = self._load_yaml()

    def _load_yaml(self):
        """內部方法：載入 YAML 文件並回傳資料"""
        if not os.path.exists(self.file_path):
            raise FileNotFoundError(f"YAML file not found at {self.file_path}")
        try:
            with open(self.file_path, 'r') as file:
                return yaml.safe_load(file)
        except Exception as e:
            raise RuntimeError(f"Error reading YAML file: {e}")

    def get_data(self):
        """取得所有 YAML 資料"""
        return self.data