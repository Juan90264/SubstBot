#!/usr/bin/python
# O nome "scriptm.py", tem o "m" com significado Matriz, sendo o script principal do bot.
# -*- coding: utf-8  -*-
"""
@ Autor: [[Usuário:Juan90264]]
@ Licença: GNU General Public License 2.0 (GPLv2)
"""

import pywikibot
from pywikibot import pagegenerators

site = pywikibot.Site()
cat = pywikibot.Category(site,'Categoria:!Páginas com predefinições que deveriam ser substituídas','Categoria:!Páginas com predefinições que deveriam ser substituídas pelo SustBot')
gen = pagegenerators.CategorizedPageGenerator(cat)
for page in gen:
    #A configuração para adicionar {{SUBST: nas páginas nas categorias selecionadas
    text = page.text
   
page.text = u"SUBST:"
page.save = u"Bot: adicionando [[WP:SUBST|SUBST]] numa predefinição"


-----------------------------------------------------------------------------------------------------------
site = pywikibot.Site()

# A configuração para adicionar {{SUBST: nas páginas de discussão de usuários
 python pwb.py add_text -cat:"!Páginas com predefinições que deveriam ser substituídas" 
-summary:"Bot: adicionando [[WP:SUBST|SUBST]] numa predefinição" \ -text:"SUBST:" -except:"\{\{([Ss]subst:|)"

      
# Ao salvar em modo teste
if testar:
  test = u'# Teste de arquivo.py #\n'
  
if testar:
   test += u'\n###### {} ({}) ######\n'.format(page.title(), u'adicionando [[WP:SUBST|SUBST]] numa predefinição'.format(title, revid)) + page.text
    else:
      page.save(u'Bot: adicionando [[WP:SUBST|SUBST]] numa predefinição'.format(title, revid))

if testar:
  with codecs.open('teste.txt', 'w', 'utf-8') as f:
    f.write(test)
    
    
    
