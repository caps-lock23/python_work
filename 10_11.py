from pathlib import Path
import json

path = Path('favorite.py')
favorite_number = input('What is your favorite number? ')
contents = json.dumps(favorite_number)
path.write_text(contents)