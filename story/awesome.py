# -*- coding: utf-8 -*-
from random import choice, randint


left = (
    'admiring', 'adoring', 'affectionate', 'amazing', 'lekker',
    'awesome', 'blissful', 'brave', 'charming', 'clever',
    'cool', 'compassionate', 'competent', 'condescending',
    'confident', 'crazy', 'dazzling', 'determined', 'distracted',
    'dreamy', 'eager', 'ecstatic', 'elastic', 'elated', 'elegant', 'eloquent',
    'epic', 'fervent', 'festive', 'flamboyant', 'focused', 'friendly',
    'frosty', 'gallant', 'gifted', 'goofy', 'gracious', 'happy', 'hardcore',
    'heuristic', 'hopeful', 'hungry', 'infallible', 'inspiring', 'jolly',
    'jovial', 'keen', 'kind', 'laughing', 'loving', 'lucid', 'magical',
    'mystifying', 'modest', 'musing', 'naughty', 'nifty', 'nostalgic',
    'objective', 'optimistic', 'peaceful', 'pedantic', 'pensive', 'practical',
    'priceless', 'quirky', 'quizzical', 'recursing', 'relaxed', 'reverent',
    'romantic', 'serene', 'sharp', 'silly', 'sleepy',
    'stoic', 'stupefied', 'suspicious', 'sweet', 'tender', 'thirsty',
    'trusting', 'unruffled', 'upbeat', 'vibrant', 'vigilant', 'vigorous',
    'wizardly', 'wonderful', 'xenodochial', 'youthful', 'zealous', 'zen'
)

right = (
    'albattani', 'allen', 'almeida', 'antonelli', 'agnesi', 'archimedes',
    'ardinghelli', 'aryabhata', 'austin', 'babbage', 'banach', 'banzai',
    'bardeen', 'bartik', 'bassi', 'beaver', 'bell', 'benz', 'bhabha',
    'bhaskara', 'blackburn', 'blackwell', 'bohr', 'booth', 'borg', 'bose',
    'boyd', 'brahmagupta', 'brattain', 'brown', 'buck', 'burnell', 'cannon',
    'carson', 'cartwright', 'chandrasekhar', 'chaplygin', 'chatelet',
    'chatterjee', 'chebyshev', 'cohen', 'chaum', 'clarke',
    'colden', 'cori', 'cray', 'curran', 'curie', 'darwin', 'davinci',
    'dewdney', 'dhawan', 'diffie', 'dijkstra', 'dirac', 'driscoll', 'dubinsky',
    'easley', 'edison', 'einstein', 'elbakyan', 'elgamal', 'elion', 'ellis',
    'engelbart', 'euclid', 'euler', 'faraday', 'feistel', 'fermat',
    'fermi', 'feynman', 'franklin', 'gagarin', 'galileo', 'galois', 'ganguly',
    'gates', 'gauss', 'germain', 'goldberg', 'goldstine', 'goldwasser',
    'golick', 'goodall', 'greider', 'grothendieck', 'haibt', 'hamilton',
    'haslett', 'hawking', 'hellman', 'heisenberg', 'hermann', 'herschel',
    'hertz', 'heyrovsky', 'hodgkin', 'hofstadter', 'hoover', 'hopper', 'hugle',
    'hypatia', 'ishizaka', 'jackson', 'jang', 'jennings', 'jepsen', 'johnson',
    'joliot', 'jones', 'kalam', 'kapitsa', 'kare', 'keldysh', 'keller',
    'kepler', 'khayyam', 'khorana', 'kilby', 'kirch', 'knuth', 'kowalevski',
    'lalande', 'lamarr', 'lamport', 'leakey', 'leavitt', 'lederberg',
    'lehmann', 'lewin', 'lichterman', 'liskov', 'lovelace', 'lumiere',
    'mahavira', 'margulis', 'matsumoto', 'maxwell', 'mayer', 'mccarthy',
    'mcclintock', 'mclaren', 'mclean', 'mcnulty', 'mendel', 'mendeleev',
    'meitner', 'meninsky', 'merkle', 'mestorf', 'minsky', 'mirzakhani',
    'moore', 'morse', 'murdock', 'moser', 'napier', 'nash', 'neumann',
    'newton', 'nightingale', 'nobel', 'noether', 'northcutt', 'noyce',
    'panini', 'pare', 'pascal', 'pasteur', 'payne', 'perlman', 'pike',
    'poincare', 'poitras', 'proskuriakova', 'ptolemy', 'raman', 'ramanujan',
    'ride', 'montalcini', 'ritchie', 'rhodes', 'robinson', 'roentgen',
    'rosalind', 'rubin', 'saha', 'sammet', 'sanderson', 'shannon', 'shaw',
    'shirley', 'shockley', 'shtern', 'sinoussi', 'snyder', 'solomon', 'spence',
    'sutherland', 'stallman', 'stonebraker', 'swanson', 'swartz', 'swirles',
    'taussig', 'tereshkova', 'tesla', 'tharp', 'thompson', 'torvalds',
    'tu', 'turing', 'varahamihira', 'vaughan', 'visvesvaraya', 'volhard',
    'villani', 'wescoff', 'wiles', 'williams', 'williamson', 'wilson',
    'wing', 'wozniak', 'wright', 'wu', 'yalow', 'yonath', 'zhukovsky'
)


def new():
    return f'{choice(left)}-{choice(right)}-{randint(1000, 9999)}'
