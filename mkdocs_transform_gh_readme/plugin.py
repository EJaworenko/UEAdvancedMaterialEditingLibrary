from mkdocs.plugins import BasePlugin
from pathlib import Path
import re
import time

class ReadmeTransformPlugin(BasePlugin):
    def __init__(self):
        self.last_update_time = 0
        self.minimum_interval = 1  # Minimum seconds between updates

    def on_pre_build(self, config):
        """Transform README before build"""
        current_time = time.time()

        # Only proceed if enough time has passed since last update
        if current_time - self.last_update_time < self.minimum_interval:
            return

        readme_path = Path('README.md')
        index_path = Path('docs/index.md')

        # Check if README exists and is newer than index.md
        if not readme_path.exists():
            return

        readme_mtime = readme_path.stat().st_mtime
        if index_path.exists():
            index_mtime = index_path.stat().st_mtime
            if readme_mtime <= index_mtime:
                return

        # Read README content
        with open(readme_path, 'r', encoding='utf-8') as f:
            lines = f.readlines()

        # Process lines
        filtered_lines = []
        skip_next_line = False
        for line in lines:
            if '<!-- omit in index.md -->' in line:
                skip_next_line = True
                continue

            if skip_next_line:
                # When skipping both index and toc, skip the next line
                if '<!-- omit in toc -->' in line:
                    continue
                skip_next_line = False
                continue

            # Replace paths that start with docs/
            line = re.sub(r'\(docs/', r'(', line)
            filtered_lines.append(line)

        # Write transformed content to index.md
        with open(index_path, 'w', encoding='utf-8') as f:
            f.writelines(filtered_lines)

        self.last_update_time = current_time
        print("Updated docs/index.md from README.md")