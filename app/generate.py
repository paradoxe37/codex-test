import os
os.makedirs('app/templates', exist_ok=True)
open('app/templates/about.html','w').write('<h1>About page</h1>')
open('app/templates/services.html','w').write('<h1>Services page</h1>')
open('app/templates/contact.html','w').write('<h1>Contact page</h1>')
