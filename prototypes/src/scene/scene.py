"""Who we gather: one floor of 1680 Mission drawn as a cutaway, ten people each doing what their group does.
Line style follows the building drawing (thin grey ink, light fills, a little hatching) and the labels follow
the exploded-diagram reference (mono labels, hairline leaders with a soft elbow)."""

INK = '#6A6E76'      # outlines
FAR = '#D5D7DF'      # far-side limbs
NEAR = '#ECEDF1'     # near-side limbs, skin-ish neutral
CLOTH = '#E2E3EA'
DARK = '#9EA2AC'     # hair, shoes
WALL = '#B9BCC3'     # room lines
ACC = '#E9A23B'      # warm accent (gold, like the reference)
SIG = '#EB5809'      # signal orange, used sparingly
LEAD = '#BFC2C8'     # leader lines
LBL = '#5F636B'

W, H = 1640, 566
FLOOR = 470

out = []
def add(s): out.append(s)

def line(x1, y1, x2, y2, w=1.4, c=INK, extra=''):
    add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{c}" stroke-width="{w}" stroke-linecap="round" {extra}/>')

def poly(pts, fill=NEAR, w=1.4, c=INK, close=True, extra=''):
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts) + (' Z' if close else '')
    add(f'<path d="{d}" fill="{fill if close else "none"}" stroke="{c}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" {extra}/>')

def path(d, fill='none', w=1.4, c=INK, extra=''):
    add(f'<path d="{d}" fill="{fill}" stroke="{c}" stroke-width="{w}" stroke-linejoin="round" stroke-linecap="round" {extra}/>')

def rect(x, y, w_, h_, fill=NEAR, r=2, w=1.4, c=INK, extra=''):
    add(f'<rect x="{x}" y="{y}" width="{w_}" height="{h_}" rx="{r}" fill="{fill}" stroke="{c}" stroke-width="{w}" {extra}/>')

def circ(x, y, r, fill=NEAR, w=1.4, c=INK, extra=''):
    add(f'<circle cx="{x}" cy="{y}" r="{r}" fill="{fill}" stroke="{c}" stroke-width="{w}" {extra}/>')

def limb(pts, width, fill):
    """An outlined limb: a fat ink stroke, then a slightly thinner fill stroke on top."""
    d = 'M' + ' L'.join(f'{x},{y}' for x, y in pts)
    add(f'<path d="{d}" fill="none" stroke="{INK}" stroke-width="{width + 2.8}" stroke-linecap="round" stroke-linejoin="round"/>')
    add(f'<path d="{d}" fill="none" stroke="{fill}" stroke-width="{width}" stroke-linecap="round" stroke-linejoin="round"/>')

def hatch(x, y, w_, h_, step=5, c=WALL):
    """Diagonal pencil hatching, like the shadows in the building drawing."""
    add(f'<g stroke="{c}" stroke-width=".8" opacity=".7">')
    i = 0
    while i < w_ + h_:
        x1, y1 = x + max(0, i - h_), y + min(h_, i)
        x2, y2 = x + min(w_, i), y + max(0, i - w_)
        add(f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>')
        i += step
    add('</g>')

def shadow(cx, w_):
    add(f'<ellipse cx="{cx}" cy="{FLOOR + 2}" rx="{w_}" ry="5" fill="#000" opacity=".06"/>')

def person(j, face=1, hair='short', top=CLOTH, legs=FAR):
    """j: joints. face = 1 looks right, -1 looks left. Far limbs first, then body, then near limbs."""
    # far leg + far arm
    limb([j['hip'], j['fk'], j['ff']], 11, legs)
    add(f'<ellipse cx="{j["ff"][0] + 4 * face}" cy="{j["ff"][1] + 1}" rx="7" ry="3.6" fill="{DARK}" stroke="{INK}" stroke-width="1.2"/>')
    limb([j['sh'], j['fe'], j['fh']], 8.5, FAR)
    circ(j['fh'][0], j['fh'][1], 4, FAR, 1.2)
    # torso
    limb([j['hip'], j['neck']], 22, top)
    # near leg
    limb([j['hip'], j['nk'], j['nf']], 11, legs)
    add(f'<ellipse cx="{j["nf"][0] + 4 * face}" cy="{j["nf"][1] + 1}" rx="7" ry="3.6" fill="{DARK}" stroke="{INK}" stroke-width="1.2"/>')
    # head
    hx, hy = j['head']
    line(j['neck'][0], j['neck'][1], hx - 2 * face, hy + 10, 6, INK)
    line(j['neck'][0], j['neck'][1], hx - 2 * face, hy + 10, 3.4, NEAR)
    circ(hx, hy, 11.5, NEAR, 1.4)
    if hair == 'short':
        path(f'M{hx - 11 * face},{hy + 2} Q{hx - 12 * face},{hy - 13} {hx + 2 * face},{hy - 11.5} Q{hx + 10 * face},{hy - 10} {hx + 11 * face},{hy - 3} Q{hx},{hy - 6} {hx - 5 * face},{hy - 1} Z', DARK, 1.2)
    elif hair == 'long':
        path(f'M{hx + 9 * face},{hy - 6} Q{hx},{hy - 16} {hx - 11 * face},{hy - 5} Q{hx - 15 * face},{hy + 10} {hx - 12 * face},{hy + 18} L{hx - 4 * face},{hy + 14} Q{hx - 6 * face},{hy + 2} {hx},{hy - 3} Q{hx + 5 * face},{hy - 2} {hx + 9 * face},{hy - 6} Z', DARK, 1.2)
    elif hair == 'bun':
        circ(hx - 8 * face, hy - 10, 5.5, DARK, 1.2)
        path(f'M{hx - 11 * face},{hy + 1} Q{hx - 11 * face},{hy - 12} {hx + 1 * face},{hy - 11.5} Q{hx + 10 * face},{hy - 9} {hx + 11 * face},{hy - 2} Q{hx},{hy - 5} {hx - 6 * face},{hy + 1} Z', DARK, 1.2)
    elif hair == 'cap':
        path(f'M{hx - 11 * face},{hy - 1} Q{hx - 10 * face},{hy - 13} {hx + 2 * face},{hy - 12} Q{hx + 11 * face},{hy - 10} {hx + 11 * face},{hy - 3} L{hx + 19 * face},{hy - 2} L{hx + 11 * face},{hy + 0} Z', ACC, 1.2)
    # eye
    circ(hx + 6 * face, hy, .9, INK, 0)
    # near arm
    limb([j['sh'], j['ne'], j['nh']], 8.5, top)
    circ(j['nh'][0], j['nh'][1], 4.2, NEAR, 1.2)

def P(**k):
    return k

# ----------------------------------------------------------------- room
def room():
    add('<g class="room">')
    # ceiling slab + floor slab, cut like a section through the building
    hatch(20, 52, W - 40, 14, 6)
    line(20, 52, W - 20, 52, 1.3, WALL); line(20, 66, W - 20, 66, 1.3, WALL)
    hatch(20, FLOOR, W - 40, 18, 6)
    line(20, FLOOR, W - 20, FLOOR, 1.5, INK); line(20, FLOOR + 18, W - 20, FLOOR + 18, 1.2, WALL)
    # back wall: big steel windows like the real floors
    for wx in (60, 470, 880, 1290):
        add(f'<rect x="{wx}" y="96" width="290" height="210" fill="#F4F5F6" stroke="{WALL}" stroke-width="1.2"/>')
        for k in (1, 2):
            line(wx + 290 * k / 3, 96, wx + 290 * k / 3, 306, 1, WALL)
        line(wx, 236, wx + 290, 236, 1, WALL)
        # a few city lines in the window
        add(f'<g stroke="{WALL}" stroke-width=".8" opacity=".75"><line x1="{wx+10}" y1="214" x2="{wx+60}" y2="214"/><line x1="{wx+60}" y1="214" x2="{wx+60}" y2="190"/><line x1="{wx+60}" y1="190" x2="{wx+105}" y2="190"/><line x1="{wx+105}" y1="190" x2="{wx+105}" y2="205"/><line x1="{wx+105}" y1="205" x2="{wx+165}" y2="205"/><line x1="{wx+165}" y1="205" x2="{wx+165}" y2="176"/><line x1="{wx+165}" y1="176" x2="{wx+205}" y2="176"/><line x1="{wx+205}" y1="176" x2="{wx+205}" y2="220"/><line x1="{wx+205}" y1="220" x2="{wx+240}" y2="220"/></g>')
    # columns between windows
    for cx in (385, 795, 1205):
        add(f'<rect x="{cx}" y="66" width="50" height="{FLOOR - 66}" fill="#F7F8F8" stroke="{WALL}" stroke-width="1.2"/>')
        hatch(cx + 34, 66, 16, FLOOR - 66, 5)
    # pendant lights
    for px in (205, 615, 1025, 1435):
        line(px, 66, px, 100, 1, WALL)
        path(f'M{px - 16},{112} Q{px},{94} {px + 16},{112} Z', '#F4F5F6', 1.2, WALL)
        add(f'<circle class="glow" cx="{px}" cy="114" r="3" fill="{ACC}" opacity=".7"/>')
    # baseboard
    line(20, FLOOR - 8, W - 20, FLOOR - 8, .8, WALL)
    add('</g>')

# ----------------------------------------------------------------- vignettes
spots = {}

def founders(x):
    # whiteboard with a rising line; founder points at it
    rect(x - 70, 200, 92, 120, '#FFFFFF', 2)
    line(x - 62, 325, x - 74, FLOOR, 1.4); line(x + 14, 325, x + 26, FLOOR, 1.4)
    path(f'M{x-60},{300} L{x-38},{285} L{x-24},{290} L{x+10},{230}', 'none', 2, SIG)
    path(f'M{x+2},{230} L{x+10},{230} L{x+10},{238}', 'none', 2, SIG)
    line(x - 60, 306, x + 12, 306, 1, WALL)
    shadow(x + 52, 26)
    person(P(head=(x + 58, 272), neck=(x + 54, 290), sh=(x + 53, 298), hip=(x + 52, 362),
             fk=(x + 46, 414), ff=(x + 40, FLOOR - 4), nk=(x + 60, 416), nf=(x + 62, FLOOR - 4),
             fe=(x + 64, 330), fh=(x + 74, 352), ne=(x + 34, 280), nh=(x + 16, 246)), face=-1, hair='short')
    spots['Startup founders'] = (x - 24, 200)

def altruists(x):
    # Mox-Giving: dropping a coin into a glass jar on a small stand
    rect(x + 14, 392, 48, 8, NEAR, 1)
    line(x + 20, 400, x + 18, FLOOR, 1.4); line(x + 56, 400, x + 58, FLOOR, 1.4)
    path(f'M{x+20},{392} L{x+20},{352} Q{x+20},{344} {x+28},{344} L{x+48},{344} Q{x+56},{344} {x+56},{352} L{x+56},{392} Z', '#F6F7F8', 1.4)
    rect(x + 24, 336, 28, 8, NEAR, 1)
    for cx, cy in ((x + 30, 386), (x + 42, 386), (x + 36, 380), (x + 48, 386)):
        circ(cx, cy, 3.6, ACC, 1)
    circ(x + 38, 322, 4, ACC, 1.1)  # coin mid-drop
    add(f'<path d="M{x+44},{316} q3,-4 0,-8" stroke="{ACC}" stroke-width="1" fill="none"/>')
    # heart above, quiet
    path(f'M{x+38},{300} c-6,-8 -16,-2 -8,6 l8,7 l8,-7 c8,-8 -2,-14 -8,-6 z', '#FCE9D9', 1.2, SIG)
    shadow(x - 6, 24)
    person(P(head=(x - 4, 270), neck=(x - 6, 288), sh=(x - 6, 296), hip=(x - 8, 362),
             fk=(x - 14, 414), ff=(x - 20, FLOOR - 4), nk=(x + 0, 416), nf=(x + 4, FLOOR - 4),
             fe=(x + 8, 328), fh=(x + 14, 350), ne=(x + 14, 312), nh=(x + 34, 314)), face=1, hair='long')
    spots['Effective altruists'] = (x + 10, 256)

def researchers(x):
    # desk with two monitors: an attention-map grid and a loss curve
    rect(x - 40, 384, 130, 8, NEAR, 1)
    line(x - 32, 392, x - 32, FLOOR, 1.4); line(x + 82, 392, x + 82, FLOOR, 1.4)
    for mx, kind in ((x - 10, 'grid'), (x + 44, 'curve')):
        rect(mx - 4, 330, 52, 38, '#2B2D31', 3)
        line(mx + 22, 368, mx + 22, 384, 3, INK)
        line(mx + 12, 384, mx + 32, 384, 2, INK)
        if kind == 'grid':
            for gx in range(4):
                for gy in range(3):
                    op = (.25, .55, .9, .4, .7, .2, .95, .35, .6, .5, .8, .3)[gx * 3 + gy]
                    add(f'<rect class="px" x="{mx + 2 + gx * 10}" y="{335 + gy * 10}" width="8" height="8" fill="{ACC}" opacity="{op}"/>')
        else:
            path(f'M{mx+2},{336} Q{mx+12},{360} {mx+24},{360} T{mx+44},{362}', 'none', 1.6, ACC)
    # chair
    path(f'M{x-58},{FLOOR} L{x-56},{404} M{x-26},{FLOOR} L{x-28},{404}', 'none', 1.4)
    rect(x - 64, 398, 44, 7, CLOTH, 2)
    rect(x - 68, 344, 8, 58, CLOTH, 3)
    shadow(x - 42, 26)
    person(P(head=(x - 34, 300), neck=(x - 38, 318), sh=(x - 38, 326), hip=(x - 44, 392),
             fk=(x - 6, 394), ff=(x - 8, FLOOR - 4), nk=(x - 2, 400), nf=(x + 2, FLOOR - 4),
             fe=(x - 22, 358), fh=(x - 4, 376), ne=(x - 18, 364), nh=(x + 6, 378)), face=1, hair='bun')
    spots['Alignment researchers'] = (x + 20, 330)

def filmmakers(x):
    # camera on a tripod, operator looking through the viewfinder
    line(x + 30, 352, x + 12, FLOOR, 1.6); line(x + 30, 352, x + 48, FLOOR, 1.6); line(x + 30, 352, x + 30, FLOOR - 6, 1.6)
    rect(x + 14, 330, 40, 24, '#3A3C41', 3)
    rect(x + 54, 334, 14, 16, '#3A3C41', 2)
    circ(x + 24, 324, 7, '#3A3C41', 1.2); circ(x + 40, 324, 7, '#3A3C41', 1.2)
    circ(x + 24, 324, 2, ACC, 0); circ(x + 40, 324, 2, ACC, 0)
    add(f'<circle class="rec" cx="{x+48}" cy="{340}" r="2.2" fill="{SIG}"/>')
    shadow(x - 10, 24)
    person(P(head=(x + 2, 300), neck=(x - 4, 316), sh=(x - 4, 324), hip=(x - 12, 384),
             fk=(x - 4, 424), ff=(x - 24, FLOOR - 4), nk=(x + 6, 426), nf=(x + 2, FLOOR - 4),
             fe=(x + 6, 346), fh=(x + 16, 336), ne=(x + 4, 352), nh=(x + 16, 346)), face=1, hair='cap')
    spots['Filmmakers'] = (x + 34, 316)

def writers(x):
    # armchair, notebook on knee, pen moving
    path(f'M{x-52},{FLOOR} L{x-50},{430} M{x+34},{FLOOR} L{x+32},{430}', 'none', 1.4)
    path(f'M{x-58},{432} L{x-58},{350} Q{x-58},{336} {x-44},{336} L{x-30},{336} Q{x-20},{336} {x-20},{350} L{x-20},{404} L{x+30},{404} Q{x+40},{404} {x+40},{414} L{x+40},{432} Z', CLOTH, 1.4)
    hatch(x - 56, 340, 10, 90, 5)
    shadow(x - 10, 46)
    person(P(head=(x - 30, 330), neck=(x - 34, 346), sh=(x - 34, 354), hip=(x - 36, 404),
             fk=(x + 10, 398), ff=(x + 14, FLOOR - 4), nk=(x + 14, 392), nf=(x + 22, FLOOR - 4),
             fe=(x - 20, 386), fh=(x + 4, 384), ne=(x - 14, 380), nh=(x + 12, 376)), face=1, hair='long')
    # notebook resting on the knee
    poly([(x - 2, 386), (x + 26, 380), (x + 28, 388), (x, 394)], '#FFFFFF', 1.2)
    add(f'<g class="pen"><line x1="{x+14}" y1="{378}" x2="{x+24}" y2="{364}" stroke="{SIG}" stroke-width="2.4" stroke-linecap="round"/></g>')
    spots['Writers'] = (x + 12, 372)

def musicians(x):
    # stool, guitar, a couple of notes drifting up
    rect(x - 26, 404, 36, 7, CLOTH, 2)
    line(x - 22, 411, x - 28, FLOOR, 1.4); line(x + 6, 411, x + 12, FLOOR, 1.4)
    shadow(x - 6, 28)
    person(P(head=(x - 8, 320), neck=(x - 10, 338), sh=(x - 10, 346), hip=(x - 12, 402),
             fk=(x + 22, 404), ff=(x + 20, FLOOR - 4), nk=(x + 26, 410), nf=(x + 30, FLOOR - 4),
             fe=(x - 4, 384), fh=(x + 4, 388), ne=(x + 16, 360), nh=(x + 38, 356)), face=1, hair='short')
    # guitar body over the lap
    add(f'<g transform="rotate(-28 {x+12} {388})">')
    path(f'M{x-14},{388} q0,-17 15,-15 q8,1 12,6 q6,-5 13,-3 q12,4 9,14 q-3,11 -13,9 q-6,-1 -10,-4 q-6,6 -14,5 q-12,-2 -12,-12 z', ACC, 1.4)
    circ(x + 8, 386, 3.6, '#7A3305', 1)
    rect(x + 34, 383, 52, 6, '#C9873A', 1, 1.2)
    rect(x + 84, 381, 12, 10, '#7A3305', 2, 1.2)
    add('</g>')
    for i, (nx, ny) in enumerate(((x + 54, 312), (x + 72, 292), (x + 46, 278))):
        add(f'<g class="note n{i}"><circle cx="{nx}" cy="{ny}" r="3.4" fill="{INK}"/><line x1="{nx+3.2}" y1="{ny}" x2="{nx+3.2}" y2="{ny-14}" stroke="{INK}" stroke-width="1.3"/></g>')
    spots['Musicians'] = (x - 8, 304)

def builders(x):
    # stringing a garland of little flags between the column and a hook
    path(f'M{x-60},{150} Q{x+10},{196} {x+80},{150}', 'none', 1.1, INK)
    for i in range(8):
        t = (i + .5) / 8
        px = (1 - t) ** 2 * (x - 60) + 2 * (1 - t) * t * (x + 10) + t ** 2 * (x + 80)
        py = (1 - t) ** 2 * 150 + 2 * (1 - t) * t * 196 + t ** 2 * 150
        col = (ACC, '#F4F5F6', '#4C7D52', '#F4F5F6')[i % 4]
        poly([(px - 6, py), (px + 6, py), (px, py + 13)], col, 1)
    # step stool
    rect(x + 52, 420, 40, 6, CLOTH, 1)
    line(x + 56, 426, x + 52, FLOOR, 1.4); line(x + 88, 426, x + 92, FLOOR, 1.4)
    shadow(x + 72, 24)
    person(P(head=(x + 74, 250), neck=(x + 72, 268), sh=(x + 72, 276), hip=(x + 70, 344),
             fk=(x + 64, 384), ff=(x + 62, 418), nk=(x + 78, 384), nf=(x + 80, 418),
             fe=(x + 58, 242), fh=(x + 58, 168), ne=(x + 90, 244), nh=(x + 82, 160)), face=-1, hair='bun', top='#DCE8DD')
    spots['Community builders'] = (x + 10, 176)

def hackers(x):
    # cross-legged on a beanbag, laptop glowing, a line of code above
    path(f'M{x-50},{FLOOR} Q{x-58},{420} {x-28},{404} Q{x+4},{392} {x+28},{412} Q{x+44},{430} {x+36},{FLOOR} Z', CLOTH, 1.4)
    hatch(x - 44, 432, 70, 36, 6)
    shadow(x - 6, 46)
    person(P(head=(x - 14, 336), neck=(x - 16, 354), sh=(x - 16, 362), hip=(x - 18, 414),
             fk=(x + 8, 430), ff=(x - 12, 440), nk=(x + 14, 436), nf=(x - 6, 446),
             fe=(x - 4, 396), fh=(x + 14, 410), ne=(x - 2, 400), nh=(x + 18, 414)), face=1, hair='cap')
    poly([(x + 6, 418), (x + 38, 418), (x + 42, 422), (x + 2, 422)], '#9EA2AC', 1.2)
    poly([(x + 14, 418), (x + 38, 418), (x + 46, 392), (x + 22, 392)], '#2B2D31', 1.2)
    add(f'<text class="code" x="{x+4}" y="{378}" font-family="IBM Plex Mono,monospace" font-size="11" fill="{SIG}">{{ }}</text>')
    add(f'<rect class="cursor" x="{x+30}" y="{398}" width="5" height="2" fill="{ACC}"/>')
    spots['Hackers'] = (x - 14, 320)

def designers(x):
    # drafting easel with the start of a drawing (the Mox gem)
    line(x + 10, 300, x - 6, FLOOR, 1.5); line(x + 10, 300, x + 30, FLOOR, 1.5); line(x + 10, 300, x + 38, FLOOR - 4, 1.2)
    poly([(x - 16, 300), (x + 40, 292), (x + 46, 382), (x - 10, 392)], '#FFFFFF', 1.4)
    rect(x - 14, 388, 60, 5, NEAR, 1)
    path(f'M{x+16},{318} l12,8 l-4,22 l-8,10 l-8,-10 l-4,-22 z', 'none', 1.2, INK)
    path(f'M{x+16},{318} l0,40 M{x+4},{326} l24,0', 'none', .8, WALL)
    path(f'M{x+2},{366} l34,-4 l-6,14 l-34,4 z', 'none', 1.2, INK)
    shadow(x + 70, 24)
    person(P(head=(x + 76, 288), neck=(x + 74, 306), sh=(x + 74, 314), hip=(x + 72, 378),
             fk=(x + 66, 424), ff=(x + 60, FLOOR - 4), nk=(x + 80, 424), nf=(x + 84, FLOOR - 4),
             fe=(x + 84, 344), fh=(x + 82, 366), ne=(x + 58, 330), nh=(x + 40, 342)), face=-1, hair='short', top='#F3E1CE')
    line(x + 40, 342, x + 32, 350, 2.2, SIG)
    spots['Designers'] = (x + 16, 292)

def gamers(x):
    # two on the floor around a board game; one rolls the dice
    rect(x - 26, 440, 60, 6, '#F4F5F6', 1)
    for i in range(4):
        for k in range(1):
            pass
    add(f'<g stroke="{WALL}" stroke-width=".8"><line x1="{x-16}" y1="440" x2="{x-16}" y2="446"/><line x1="{x-4}" y1="440" x2="{x-4}" y2="446"/><line x1="{x+8}" y1="440" x2="{x+8}" y2="446"/><line x1="{x+20}" y1="440" x2="{x+20}" y2="446"/></g>')
    circ(x - 10, 434, 4, SIG, 1); poly([(x + 12, 438), (x + 16, 426), (x + 20, 438)], ACC, 1)
    add(f'<g class="die"><rect x="{x+2}" y="{404}" width="10" height="10" rx="2" fill="#fff" stroke="{INK}" stroke-width="1.2"/><circle cx="{x+7}" cy="{409}" r="1.3" fill="{INK}"/></g>')
    shadow(x - 50, 26); shadow(x + 62, 26)
    person(P(head=(x - 56, 360), neck=(x - 58, 376), sh=(x - 58, 384), hip=(x - 62, 438),
             fk=(x - 34, 446), ff=(x - 20, 458), nk=(x - 30, 452), nf=(x - 14, 462),
             fe=(x - 48, 420), fh=(x - 52, 448), ne=(x - 36, 408), nh=(x - 6, 410)), face=1, hair='long', top='#DCE8DD')
    person(P(head=(x + 64, 362), neck=(x + 66, 378), sh=(x + 66, 386), hip=(x + 68, 438),
             fk=(x + 42, 446), ff=(x + 30, 458), nk=(x + 46, 452), nf=(x + 36, 462),
             fe=(x + 54, 420), fh=(x + 50, 446), ne=(x + 52, 418), nh=(x + 40, 434)), face=-1, hair='short')
    spots['Gamers'] = (x + 4, 400)

# ----------------------------------------------------------------- labels
def labels(order):
    """Exploded-diagram labels: mono text, hairline leader that leaves the subject and elbows into the text."""
    add('<g class="labels" font-family="IBM Plex Mono,ui-monospace,monospace" font-size="20" letter-spacing=".01em">')
    for i, name in enumerate(order):
        tx, ty = spots[name]
        top = i % 2 == 0
        ly = 30 if top else 550
        y0 = ty + (-8 if top else 8)
        ey = ly - 5
        sgn = 1 if top else -1
        path(f'M{tx},{y0} L{tx},{ey + 12 * sgn} Q{tx},{ey} {tx + 12},{ey} L{tx + 26},{ey}', 'none', 1.1, LEAD)
        add(f'<circle cx="{tx}" cy="{y0}" r="2.2" fill="{LEAD}"/>')
        add(f'<text x="{tx + 34}" y="{ly}" fill="{LBL}">{name}</text>')
    add('</g>')

def build():
    out.clear()
    room()
    xs = [110, 262, 450, 600, 760, 880, 1062, 1244, 1336, 1522]
    for f, x in zip((founders, altruists, researchers, filmmakers, writers, musicians, builders, hackers, designers, gamers), xs):
        add(f'<g class="v">')
        f(x)
        add('</g>')
    labels(['Startup founders', 'Effective altruists', 'Alignment researchers', 'Filmmakers', 'Writers',
            'Musicians', 'Community builders', 'Hackers', 'Designers', 'Gamers'])
    return f'<svg class="gather" viewBox="0 0 {W} {H}" role="img" aria-labelledby="gt"><title id="gt">One floor of Mox with startup founders, effective altruists, alignment researchers, filmmakers, writers, musicians, community builders, hackers, designers and gamers</title>' + ''.join(out) + '</svg>'

if __name__ == '__main__':
    svg = build()
    open('scene.html', 'w').write('<!doctype html><meta charset=utf-8><body style="margin:0;background:#F9FAFA">' + svg.replace('<svg ', '<svg width="1640" ') + '</body>')
    print(len(svg))
