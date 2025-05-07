# Create README.md
echo "# AI Honeypot" > README.md

# Create LICENSE file with MIT license
curl -o LICENSE https://raw.githubusercontent.com/github/choosealicense.com/gh-pages/_licenses/mit.txt

# Stage and commit
git add README.md LICENSE
git commit -m "Add README and LICENSE"
git push origin main

