#!/usr/bin/python
# This script contains the defaults to be overwritten on execution.
# To start the bot, I will use the "python pwb.py replace -fix:checksubst -start -ns:3 -sleep:2 -always"
# -*- coding: utf-8  -*-
"""
@ Autor: [[Usuário:Juan90264]]
@ Licença: GNU General Public License 2.0 (GPLv2)
"""

if 'fixes' not in globals(): fixes = {}

fixes['checksubst'] = {
    'regex': True,
    'msg': {
        '_default': 'Bot: adding SUBST to some templates',
    },
    'replacements': [
    (r'\{\{[Ww]elcome', r'{{SUBST:Welcome'),
    (r'\{\{[Ww]elcome-anon', r'{{SUBST:Welcome-anon'),
    (r'\{\{[Ww]elcome-belated', r'{{SUBST:Welcome-belated'),
    (r'\{\{[Uu]w-block', r'{{SUBST:Uw-block'),
    (r'\{\{[Uu]ndated', r'{{SUBST:Undated'),
    (r'\{\{[Tt]ls', r'{{SUBST:Tls'),
    (r'\{\{[Tt]axotemp', r'{{SUBST:Taxotemp'),
    (r'\{\{[Nn]oi', r'{{SUBST:Noi'),
    (r'\{\{[Rr]eftemp', r'{{SUBST:Reftemp'),
    (r'\{\{[Ii]no', r'{{SUBST:Ino'),
    (r'\{\{[Aa]utopatrolled', r'{{SUBST:Autopatrolled'),
    (r'\{\{[Aa]lgaeBase', r'{{SUBST:[Aa]lgaeBase'), 
    (r'\{\{[Ss]hared IP advice', r'{{SUBST:Shared IP advice')
    ]
}


