#!/usr/bin/python
# O nome "scriptm.py", tem o "m" com significado Matriz, sendo o script principal do bot.
# -*- coding: utf-8  -*-
"""
@ Autor: [[Usuário:Juan90264]]
@ Licença: GNU General Public License 2.0 (GPLv2)
"""

import pywikibot, css, re, time, codecs

# Ao ativar o modo testar a configuração é lida na mesma pasta e as edições 
# que seriam feitas salvas em teste.txt, nenhuma edição é feita na Wikipédia.
testar = False

site = pywikibot.Site()

# A configuração

if testar:
  test = u'# Teste de arquivo.py #\n'
  
if testar:
   test += u'\n###### {} ({}) ######\n'.format(page.title(), u'adicionando [[WP:SUBST|SUBST]] numa predefinição'.format(title, revid)) + page.text
    else:
      page.save(u'Bot: adicionando [[WP:SUBST|SUBST]] numa predefinição'.format(title, revid))

if testar:
  with codecs.open('teste.txt', 'w', 'utf-8') as f:
    f.write(test)  
