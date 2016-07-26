# -*- coding: utf-8 -*-
from __future__ import unicode_literals

FIRST_NAME_TITLES = set([
    'aunt',
    'auntie',
    'brother',
    'dame',
    'father',
    'king',
    'maid',
    'master',
    'mother',
    'pope',
    'queen',
    'sir',
    'sister',
    'uncle',
    'sheikh',
    'sheik',
    'shaik',
    'shayk',
    'shaykh',
    'shaikh',
    'cheikh',
    'shekh',
])
"""
When these titles appear with a single other name, that name is a first name, e.g.
"Sir John", "Sister Mary", "Queen Elizabeth".
"""

#: **Cannot include things that could also be first names**, e.g. "dean".
#: Many of these from wikipedia: https://en.wikipedia.org/wiki/Title.
#: The parser recognizes chains of these including conjunctions allowing 
#: recognition titles like "Deputy Secretary of State".
TITLES = FIRST_NAME_TITLES | set([
    "attaché",
    "chargé d'affaires",
    "king's",
    "marchioness",
    "marquess",
    "marquis",
    "marquise",
    "queen's",
    '1lt',
    '1sgt',
    '1stlt',
    '1stsgt',
    '2lt',
    '2ndlt',
    'a1c',
    'ab',
    'abbess',
    'abbot',
    'academic',
    'acolyte',
    'adept',
    'adjutant',
    'adm',
    'admiral',
    'advocate',
    'air',
    'akhoond',
    'alderman',
    'almoner',
    'ambassador',
    'amn',
    'analytics',
    'appellate',
    'apprentice',
    'arbitrator',
    'archbishop',
    'archdeacon',
    'archdruid',
    'archduchess',
    'archduke',
    'arhat',
    'assistant',
    'assoc',
    'associate',
    'asst',
    'attache',
    'attorney',
    'ayatollah',
    'baba',
    'bailiff',
    'banner',
    'bard',
    'baron',
    'barrister',
    'bearer',
    'bench',
    'bg',
    'bgen',
    'blessed',
    'bodhisattva',
    'brigadier',
    'briggen',
    'buddha',
    'burgess',
    'business',
    'bwana',
    'canon',
    'capt',
    'captain',
    'cardinal',
    'catholicos',
    'ccmsgt',
    'cdr',
    'ceo',
    'cfo',
    'chair',
    'chairs',
    'chancellor',
    'chaplain',
    'chief',
    'chieftain',
    'civil',
    'clerk',
    'cmsaf',
    'cmsgt',
    'co-chair',
    'co-chairs',
    'coach',
    'col',
    'colonel',
    'commander',
    'commander-in-chief',
    'commodore',
    'comptroller',
    'controller',
    'corporal',
    'corporate',
    'councillor',
    'courtier',
    'cpl',
    'cpo',
    'cpt',
    'credit',
    'criminal',
    'csm',
    'curator',
    'customs',
    'cwo-2',
    'cwo-3',
    'cwo-4',
    'cwo-5',
    'cwo2',
    'cwo3',
    'cwo4',
    'cwo5',
    'deacon',
    'delegate',
    'deputy',
    'designated',
    'dir',
    'director',
    'discovery',
    'district',
    'division',
    'do',
    'docent',
    'docket',
    'doctor',
    'doyen',
    'dpty',
    'dr',
    'druid',
    'duke',
    'dutchess',
    'edmi',
    'edohen',
    'effendi',
    'ekegbian',
    'elder',
    'elerunwon',
    'emperor',
    'empress',
    'ens',
    'envoy',
    'exec',
    'executive',
    'fadm',
    'family',
    'federal',
    'field',
    'financial',
    'first',
    'flag',
    'flying',
    'foreign',
    'forester',
    'friar',
    'gen',
    'general',
    'generalissimo',
    'gentiluomo',
    'giani',
    'goodman',
    'goodwife',
    'governor',
    'grand',
    'group',
    'guru',
    'gyani',
    'gysgt',
    'hajji',
    'headman',
    'her',
    'hereditary',
    'high',
    'his',
    'hon', # sorry Hon Solo, but judges seem more common.
    'honorable',
    'honourable',
    'imam',
    'information',
    'intelligence',
    'intendant',
    'journeyman',
    'jr',
    'judge',
    'judicial',
    'junior',
    'kingdom',
    'knowledge',
    'lady',
    'lama',
    'lamido',
    'law',
    'lcdr',
    'lcpl',
    'leader',
    'lieutenant',
    'lord',
    'lt',
    'ltc',
    'ltcol',
    'ltg',
    'ltgen',
    'ltjg',
    'madam',
    'madame',
    'mag',
    'mag-judge',
    'mag/judge',
    'magistrate',
    'magistrate-judge',
    'maharajah',
    'maharani',
    'mahdi',
    'maj',
    'majesty',
    'majgen',
    'manager',
    'marcher',
    'marketing',
    'matriarch',
    'mayor',
    'mcpo',
    'mcpoc',
    'mcpon',
    'md',
    'member',
    'metropolitan',
    'mg',
    'mgr',
    'mgysgt',
    'minister',
    'miss',
    'misses',
    'mister',
    'monsignor',
    'mpco-cg',
    'mr',
    'mrs',
    'ms',
    'msg',
    'msgt',
    'mufti',
    'mullah',
    'municipal',
    'murshid',
    'nanny',
    'national',
    'nurse',
    'officer',
    'operating',
    'pastor',
    'patriarch',
    'petty',
    'pfc',
    'pharaoh',
    'pilot',
    'pir',
    'po1',
    'po2',
    'po3',
    'police',
    'political',
    'prefect',
    'prelate',
    'premier',
    'pres',
    'presbyter',
    'president',
    'presiding',
    'priest',
    'priestess',
    'primate',
    'prime',
    'prin',
    'prince',
    'princess',
    'principal',
    'prior',
    'private',
    'pro',
    'prof',
    'provost',
    'pslc',
    'pursuivant',
    'pv2',
    'pvt',
    'rabbi',
    'radm',
    'rangatira',
    'ranger',
    'rdml',
    'rear',
    'rebbe',
    'registrar',
    'rep',
    'representative',
    'resident',
    'rev',
    'revenue',
    'reverend',
    'right',
    'risk',
    'royal',
    'rt',
    'sa',
    'saint',
    'saoshyant',
    'scpo',
    'se',
    'secretary',
    'security',
    'seigneur',
    'senator',
    'senior',
    'senior-judge',
    'sergeant',
    'servant',
    'sfc',
    'sgm',
    'sgt',
    'sgtmaj',
    'sgtmajmc',
    'shehu',
    'sheikh',
    'sheriff',
    'siddha',
    'sma',
    'smsgt',
    'sn',
    'solicitor',
    'spc',
    'speaker',
    'special',
    'sr',
    'sra',
    'ssg',
    'ssgt',
    'staff',
    'state',
    'states',
    'strategy',
    'subaltern',
    'subedar',
    'sultan',
    'sultana',
    'superior',
    'supreme',
    'surgeon',
    'swordbearer',
    'sysselmann',
    'tax',
    'technical',
    'timi',
    'tirthankar',
    'treasurer',
    'tsar',
    'tsarina',
    'tsgt',
    'uk',
    'united',
    'us',
    'vadm',
    'vardapet',
    'vc',
    'venerable',
    'verderer',
    'vicar',
    'vice',
    'viscount',
    'vizier',
    'warden',
    'warrant',
    'wing',
    'wo-1',
    'wo1',
    'wo2',
    'wo3',
    'wo4',
    'wo5',
    'woodman',
])
