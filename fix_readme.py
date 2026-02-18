with open('README.md', 'r') as f:
    content = f.read()

# Remove Overview Metrics table but keep streak stats
import re
pattern_overview = r'<table>\s*<tr>\s*<td width="50%" align="center">\s*<img src="https://github-readme-stats\.vercel\.app/api\?username=Raul909[^"]+" alt="GitHub Stats" />\s*</td>\s*<td width="50%" align="center">\s*(<img src="https://streak-stats\.demolab\.com\?user=Raul909[^"]+" alt="GitHub Streak" />)\s*</td>\s*</tr>\s*</table>'
replacement_overview = r'\1'
content = re.sub(pattern_overview, replacement_overview, content, flags=re.DOTALL)

# Remove Language Proficiency section
pattern_lang = r'### 💻 Language Proficiency\s*<img width="65%" src="https://github-readme-stats\.vercel\.app/api/top-langs/\?username=Raul909[^"]+" alt="Top Languages" />\s*'
content = re.sub(pattern_lang, '', content, flags=re.DOTALL)

# Remove Achievement Showcase section
pattern_achieve = r'### 🏆 Achievement Showcase\s*<img width="100%" src="https://github-profile-trophy\.vercel\.app/\?username=Raul909[^"]+" alt="GitHub Trophies" />\s*'
content = re.sub(pattern_achieve, '', content, flags=re.DOTALL)

with open('README.md', 'w') as f:
    f.write(content)
