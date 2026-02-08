import os,sys
name=sys.argv[1] if len(sys.argv)>1 else 'Mon Site'
pages=['index','about','services','contact']
os.makedirs('app/templates', exist_ok=True)
for p in pages:
    open(f'app/templates/{p}.html','w').write(f'<h1>{name} - {p}</h1><p>Page générée automatiquement 🚀</p>')
    open(f'app/templates/{p}.html','w').write(f'<h1>{name} - {p}</h1><p>Page générée automatiquement 🚀</p>')
print('LEVEL 2 MULTI OK')
