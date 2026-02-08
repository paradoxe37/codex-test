import os, sys
name = sys.argv[1] if len(sys.argv)>1 else 'Mon Site'
tagline = 'Site généré automatiquement — rapide, propre, SEO-ready.'
email = 'contact@exemple.fr'
phone = '06 00 00 00 00'
pages={'index':'Accueil','about':'A propos','services':'Services','contact':'Contact'}
nav=''.join([f"<a href='/{p}'>{t}</a>" for p,t in pages.items()])
os.makedirs('app/templates',exist_ok=True)
for p,title in pages.items():
 html=f"<html><head><title>{title} — {name}</title><link rel='stylesheet' href='/static/css/style.css'></head><body><h1>{title}</h1><p>{tagline}</p><p>{email} {phone}</p></body></html>"
 open(f'app/templates/{p}.html','w').write(html)
 open(f'app/templates/{p}.html','w').write(html)
print('LEVEL 4 OK 🚀')
