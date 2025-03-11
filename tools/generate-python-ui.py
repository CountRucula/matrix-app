import os
import subprocess
from pathlib import Path
import shutil

base_path = Path(__file__).parent

src_dir = (base_path / '../src/qt/design-files').resolve()
dst_dir = (base_path / '../src/qt/generated').resolve()

# clean-up generated folder
shutil.rmtree(dst_dir)

# generate python files
for (root,dirs,files) in os.walk(src_dir, topdown=True):
  for file in files:
    if file.endswith('.ui'):
      # get src / dst file paths
      src_file = Path(root) / file
      rel_path = src_file.relative_to(src_dir)
      dst_file = dst_dir / rel_path
      dst_file = dst_file.with_name("UI_" + file.replace('.ui', '.py'))

      # Create nested directories in the destination if needed
      dst_file.parent.mkdir(parents=True, exist_ok=True)

      # convert .ui files
      print(f'Converting ".\\{src_file}" -> ".\\{dst_file}"')
      subprocess.run(["pyside6-uic", str(src_file), "-o", str(dst_file)])