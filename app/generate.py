import os, sys
name = sys.argv[1] if len(sys.argv)>1 else 'Mon Site'
os.makedirs('app/templates', exist_ok=True)
html = f'<h1>{name}</h1><p>Site généré automatiquement 🚀</p>'
open('app/templates/index.html','w').write(html)
