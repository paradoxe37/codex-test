import os,sys
name=sys.argv[1] if len(sys.argv)>1 else 'Mon Site'
tagline=sys.argv[2] if len(sys.argv)>2 else 'Site pro généré automatiquement'
email=sys.argv[3] if len(sys.argv)>3 else 'contact@example.com'
phone=sys.argv[4] if len(sys.argv)>4 else '0600000000'
os.makedirs('app/templates', exist_ok=True)
pages=['index','about','services','contact']
nav="<a href='/'>Accueil</a> | <a href='/about'>A propos</a> | <a href='/services'>Services</a> | <a href='/contact'>Contact</a>"
for p in pages:
    title=('Accueil' if p=='index' else ('A propos' if p=='about' else ('Services' if p=='services' else 'Contact')))
    html=f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — {name}</title><meta name="description" content="{tagline}"><link rel="stylesheet" href="/static/css/style.css"></head><body><header class="hdr"><div class="wrap nav"><a class="brand" href="/">{name}</a><nav class="links">{nav}</nav></div></header><main class="wrap"><h1>{title}</h1><div class="card"><p>{tagline}</p><p><strong>Email</strong> : {email}<br><strong>Téléphone</strong> : {phone}</p></div></main><footer class="wrap ftr"><small>© {name}</small></footer></body></html>"""
for p in pages:
    title=('Accueil' if p=='index' else ('A propos' if p=='about' else ('Services' if p=='services' else 'Contact')))
    html=f"""<!doctype html><html lang="fr"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} — {name}</title><meta name="description" content="{tagline}"><link rel="stylesheet" href="/static/css/style.css"></head><body><header class="hdr"><div class="wrap nav"><a class="brand" href="/">{name}</a><nav class="links">{nav}</nav></div></header><main class="wrap"><h1>{title}</h1><div class="card"><p>{tagline}</p><p><strong>Email</strong> : {email}<br><strong>Téléphone</strong> : {phone}</p></div></main><footer class="wrap ftr"><small>© {name}</small></footer></body></html>"""
    open(f'app/templates/{p}.html','w').write(html)
print('LEVEL 3 OK')
