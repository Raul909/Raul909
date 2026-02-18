with open('README.md', 'r') as f:
    content = f.read()

# Replace the mangled string with the correct one
correct_url = "https://leetcard.jacoblin.cool/Raul5756?theme=dark&font=source_code_pro&extension=null&width=500"
# The mangled string is what grep showed: "https://leetcard.jacoblin.cool/Raul5756?theme=darkhttps://leetcode.card.workers.dev/Raul5756?theme=dark&font=source_code_pro&extension=null&width=500font=source_code_prohttps://leetcode.card.workers.dev/Raul5756?theme=dark&font=source_code_pro&extension=null&width=500extension=nullhttps://leetcode.card.workers.dev/Raul5756?theme=dark&font=source_code_pro&extension=null&width=500width=500"

# It's better to search for the pattern surrounding it to be safe
start_marker = "[![LeetCode Stats]("
end_marker = ")](https://leetcode.com/Raul5756/)"

import re
pattern = r'\[!\[LeetCode Stats\]\([^)]+\)\]\(https://leetcode\.com/Raul5756/\)'
match = re.search(pattern, content)
if match:
    replacement = f"[![LeetCode Stats]({correct_url})](https://leetcode.com/Raul5756/)"
    content = content.replace(match.group(0), replacement)

with open('README.md', 'w') as f:
    f.write(content)
