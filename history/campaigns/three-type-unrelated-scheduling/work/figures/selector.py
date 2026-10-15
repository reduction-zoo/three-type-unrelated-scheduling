from pathlib import Path
from html import escape

points=[(x,y,z) for x in range(9) for y in range(8) for z in range(4) if 4*x+5*y+9*z==35]
assert sorted(points)==[(0,7,0),(2,0,3),(3,1,2),(4,2,1),(5,3,0)]
assert [v for v in points if 7*v[0]+2*v[1]<=14]==[(0,7,0),(2,0,3)]
s=['<svg xmlns="http://www.w3.org/2000/svg" width="640" height="395" viewBox="0 0 640 395"><rect width="640" height="395" fill="white"/><g font-family="Times New Roman,serif" font-size="18" fill="#202020">']
s.append('<path d="M70 280 L226 85 L460 280 Z" fill="#eeeeee" stroke="#505050" stroke-width="1.5"/><path d="M70 280 L226 85" stroke="#153c70" stroke-width="3"/>')
s.append('<path d="M70 25 V280 H570" fill="none" stroke="#202020" stroke-width="1.5"/>')
for x in range(6):
    X=70+78*x
    s.append(f'<path d="M{X} 280 v6" stroke="#202020"/><text x="{X}" y="307" text-anchor="middle">{x}</text>')
for z in range(1,4):
    Y=280-65*z
    s.append(f'<path d="M70 {Y} h-6" stroke="#202020"/><text x="56" y="{Y+6}" text-anchor="end">{z}</text>')
labels={(0,7,0):(110,263,'start'),(2,0,3):(240,78,'start'),(3,1,2):(317,139,'start'),(4,2,1):(394,204,'start'),(5,3,0):(500,265,'start')}
for x,y,z in points:
    X,Y=70+78*x,280-65*z
    if y in (7,0):s.append(f'<circle cx="{X}" cy="{Y}" r="5.5" fill="#153c70"/>')
    else:s.append(f'<path d="M{X-5} {Y-5} l10 10 m0 -10 l-10 10" stroke="#202020" stroke-width="2.5"/>')
    lx,ly,anchor=labels[x,y,z]
    prefix='u = ' if y==7 else 'v = ' if y==0 else ''
    s.append(f'<text x="{lx}" y="{ly}" text-anchor="{anchor}">{escape(prefix+str((x,y,z)))}</text>')
s.append('<text x="90" y="44">k = 4, a = 2</text><text x="90" y="70">4x + 5y + 9z = 35</text><text x="320" y="337" text-anchor="middle">Type-one count x</text><text transform="translate(23,167) rotate(-90)" text-anchor="middle">Type-three count z</text>')
s.append('<circle cx="105" cy="373" r="5.5" fill="#153c70"/><text x="122" y="379" font-size="17">Retained configurations</text><path d="M345 368 l10 10 m0 -10 l-10 10" stroke="#202020" stroke-width="2.5"/><text x="367" y="379" font-size="17">Excluded configurations</text></g></svg>')
Path(__file__).with_name('selector.svg').write_text(''.join(s))
print('Verified five objective-fiber points; exactly two retained configurations.')
