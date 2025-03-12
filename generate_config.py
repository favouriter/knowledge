import os
import json
from pathlib import Path

def get_title(file_path):
    # 从文件内容中提取标题
    if file_path.suffix == '.md':
        with open(file_path, 'r', encoding='utf-8') as f:
            first_line = f.readline()
            return first_line.strip('# \n') or file_path.stem
    return file_path.stem  # 其他格式直接使用文件名

def scan_directory(root_dir):
    def _scan(path):
        entry = {
            "name": path.name,
            "path": str(path.relative_to(root_dir)),
            "subcategories": [],
            "articles": []
        }
        
        for item in path.iterdir():
            if item.is_dir():
                entry["subcategories"].append(_scan(item))
            elif item.suffix.lower() in ('.md', '.pdf', '.html'):
                entry["articles"].append({
                    "type": item.suffix[1:].lower(),
                    "title": get_title(item),
                    "path": str(item.relative_to(root_dir))
                })
        return entry
    
    return _scan(Path(root_dir))

if __name__ == "__main__":
    config = {
        "categories": scan_directory("docs/articles").get("subcategories", [])
    }
    
    with open("docs/config.json", "w", encoding='utf-8') as f:
        json.dump(config, f, ensure_ascii=False, indent=2)