from pathlib import Path
import json

path = Path('favorite.py')
content = path.read_text()
favorite_number = json.loads(content)

print(f"I know your favorite number! It's : {favorite_number}")