"""Generates the retro-sidebar avatar GIFs.

Each character is hand-drawn pixel art: a grid of letters where every letter
is a palette color and "." is transparent. Eyes and mouth are small patches
painted over the base, so one drawing gives every expression. Each state
(working, blocked, done, idle) is a short list of frames built from the same
drawing plus movement (bob, shake, jump) and effects (tokens, "!", sparkles,
"z").

Run with any Python that has Pillow:
    python generate.py
It writes <character>-<variant>-<state>.gif next to this file.
"""

from pathlib import Path

from PIL import Image

OUT = Path(__file__).parent
SCALE = 4  # every art pixel becomes a 4x4 block: crisp at 2x screens
W, H = 28, 26  # canvas, in art pixels
BODY_X, BODY_Y = 2, 7  # where the 18x17 body sits on the canvas

# ---------------------------------------------------------------------------
# Characters. Every body is 18 columns x 17 rows.

SPARKY = {
    "art": [
        "......KKKKKK......",
        "....KKOOOOOOKK....",
        "...KOPPOOOOOOOK...",
        "..KOPPOOOOOOOOOK..",
        "..KOOOOOOOOOOOOK..",
        ".KOOOkkOOOOkkOOOK.",
        ".KOOOkWOOOOkWOOOK.",
        ".KOOOkkOOOOkkOOOK.",
        ".KORROOOOOOOORROK.",
        ".KOOOOOKOOKOOOOOK.",
        ".KOOOOOOKKOOOOOOK.",
        ".KoOOOOOOOOOOOOoK.",
        "KoKoOOOOOOOOOOoKoK",
        "KK.KoOOOOOOOOoK.KK",
        "...KKoooKKoooKK...",
        "....KooK..KooK....",
        "....KKKK..KKKK....",
    ],
    "eyes": [(5, 5), (11, 5)],  # top-left of each 2x3 eye
    "eye_shut": ["OO", "kk", "OO"],
    "mouth": (7, 9),  # top-left of the 4x2 mouth
    "mouths": {
        "smile": ["KOOK", "OKKO"],
        "open": ["KKKK", "KrrK"],
        "gasp": ["OKKO", "OKKO"],
    },
    "tokens": "side",
    "variants": {
        "amber": {"O": "#d97757", "o": "#b25a3c", "P": "#f4b08f"},
        "lilac": {"O": "#a58bf0", "o": "#7a62c9", "P": "#cdbdfb"},
        "mint": {"O": "#6fd3b0", "o": "#47a888", "P": "#b5f0dc"},
    },
    # Where accessories go, in body coordinates.
    "anchors": {"head_top": 0, "hat_x": 5, "bow": (11, -1), "eye_y": 5, "neck_y": 11, "neck": (2, 15)},
}

BYTE = {
    "art": [
        "..KKKKKKKKKKKKKK..",
        ".KCCCCCCCCCCCCCcK.",
        ".KCKKKKKKKKKKKKcK.",
        ".KCKSSSSSSSSSSKcK.",
        ".KCKSGGSSSSGGSKcK.",
        ".KCKSGGSSSSGGSKcK.",
        ".KCKSSSSSSSSSSKcK.",
        ".KCKSSSGSSGSSSKcK.",
        ".KCKSSSSGGSSSSKcK.",
        ".KCKSSSSSSSSSSKcK.",
        ".KCKKKKKKKKKKKKcK.",
        ".KCCCCCCCCCRCCCcK.",
        ".KccccccccccccccK.",
        "..KKKKKKKKKKKKKK..",
        "...KcK......KcK...",
        "..KKcK......KcKK..",
        "..KKKK......KKKK..",
    ],
    "eyes": [(5, 4), (11, 4)],  # 2x2 eyes on the screen
    "eye_shut": ["SS", "GG"],
    "mouth": (7, 7),
    "mouths": {
        "smile": ["GSSG", "SGGS"],
        "open": ["GGGG", "GSSG"],
        "gasp": ["SGGS", "SGGS"],
    },
    "tokens": "top",  # coins drop into a slot on top of the case
    "slot": 8,
    "variants": {
        "beige": {"C": "#e8dcc0", "c": "#bfae8c", "S": "#163328", "G": "#6ef0a0"},
        "noir": {"C": "#4a4a5e", "c": "#33334a", "S": "#101626", "G": "#7cc7ff"},
        "rose": {"C": "#f2c6d4", "c": "#c996a8", "S": "#2a1630", "G": "#ff9ad5"},
    },
    "anchors": {"head_top": 0, "hat_x": 5, "bow": (12, -2), "eye_y": 4, "neck_y": 11, "neck": (2, 15)},
}

EMBER = {
    "art": [
        "......H....H......",
        ".....KHK..KHK.....",
        "....KNNNKKNNNK....",
        "...KNNNNNNNNNNK...",
        "..KNNNNNNNNNNNNK..",
        "..KNNkkNNNNkkNNNK.",
        "..KNNkWNNNNkWNNNNK",
        "..KNNkkNNNNkkNNNNK",
        "..KNRRNNNNNNNNNNNK",
        ".TKNNNNNNNNNNNNNK.",
        "TTKNNNNNNKKKNNNK..",
        "TtTKNBBBBBBBNNK...",
        ".TtKNBBBBBBBNNK...",
        "..TKNNBBBBBNNNK.KK",
        "...KNNNNNNNNNNKKNK",
        "....KnnK..KnnKKK..",
        "....KKKK..KKKK....",
    ],
    "eyes": [(5, 5), (11, 5)],
    "eye_shut": ["NN", "kk", "NN"],
    "mouth": (9, 9),
    "mouths": {
        "smile": ["NNNN", "KKKN"],
        "open": ["KKKK", "KrrK"],
        "gasp": ["NKKN", "NKKN"],
    },
    "tokens": "side",
    "variants": {
        "moss": {"N": "#5cc98a", "n": "#3a9a63", "T": "#4fb3a9", "t": "#2f7f78"},
        "flame": {"N": "#e8664f", "n": "#b24433", "T": "#f2a24a", "t": "#c47a2c"},
        "frost": {"N": "#7cc0f0", "n": "#4f8fc4", "T": "#b49cf0", "t": "#8a72c9"},
    },
    "anchors": {"head_top": 2, "hat_x": 5, "bow": (12, 0), "eye_y": 5, "neck_y": 10, "neck": (3, 14)},
}

NOVA = {
    # An octopus astronaut: its head inside a glass helmet, four tentacles below.
    "art": [
        "....KKKKKKKKKK....",
        "...KVwVVVVVVVVK...",
        "..KVwKKKKKKKKVVK..",
        ".KVwKQQQQQQQQKVVK.",
        ".KVKQQQQQQQQQQKVK.",
        ".KVKQkkQQQQkkQKVK.",
        ".KVKQkWQQQQkWQKVK.",
        ".KVKQkkQQQQkkQKVK.",
        ".KVKRQQQQQQQQRKVK.",
        ".KVKQQQQQQQQQQKVK.",
        "..KVKQQQQQQQQKVK..",
        "..KvvvvvvvvvvvvK..",
        "...KQQKQQKQQKQQK..",
        "...KQqKQqKQqKQqK..",
        "...KqQKqQKqQKqQK..",
        ".KQqK..KK.KK.KqQK.",
        ".KK............KK.",
    ],
    "eyes": [(5, 5), (11, 5)],
    "eye_shut": ["QQ", "kk", "QQ"],
    "mouth": (7, 8),
    "mouths": {
        "smile": ["KQQK", "QKKQ"],
        "open": ["KKKK", "KrrK"],
        "gasp": ["QKKQ", "QKKQ"],
    },
    "tokens": "tentacle",  # a tentacle catches the coin low, then lifts it to the mouth
    "variants": {
        "grape": {"Q": "#b07be8", "q": "#8452c0", "V": "#d6efff", "v": "#a3adc9"},
        "coral": {"Q": "#ff8a70", "q": "#d1604a", "V": "#d6efff", "v": "#e8c26a"},
        "sun": {"Q": "#f2c14e", "q": "#c99528", "V": "#d6efff", "v": "#a3adc9"},
    },
    "anchors": {"head_top": 0, "hat_x": 5, "bow": (12, -1), "eye_y": 5, "neck_y": 11, "neck": (3, 14)},
}

CHARACTERS = {"sparky": SPARKY, "byte": BYTE, "ember": EMBER, "nova": NOVA}

# Colors every drawing shares.
BASE = {
    "K": "#1b1428",  # outline
    "k": "#1b1428",  # eye
    "W": "#ffffff",  # eye shine
    "R": "#ff8fa3",  # blush / power led
    "r": "#e05570",  # tongue
    "B": "#f3e3a0",  # belly
    "H": "#f5d27a",  # horns
    "Y": "#ffd34d",  # token / sparkle
    "y": "#fff3b0",  # token shine
    "Z": "#b9b4d6",  # sleep z
    "X": "#ff5c74",  # alert mark
    "w": "#ffffff",  # bubble
}

# ---------------------------------------------------------------------------
# Accessories: small drawings placed on a character's anchors. "F" and "f" are
# the accessory's own colors, "L" and "l" a lens and its shine.

ACCESSORIES = {
    "plain": {},
    "beanie": {"F": "#e05570", "f": "#b23a55"},
    "bow": {"F": "#ff8fc8", "f": "#d8609e"},
    "shades": {"F": "#ff5c74", "L": "#1b1428", "l": "#6cb6ff"},
    "headphones": {"F": "#6cb6ff", "f": "#3f7fc4"},
    "scarf": {"F": "#ffd34d", "f": "#e8a23a"},
}

BEANIE = ["...ww...", "..FFFF..", ".FFFFFF.", ".ffffff."]
BOW = ["FF.FF", "FFfFF", "FF.FF"]
# A colored frame over dark lenses, so they show on dark faces too.
SHADES = ["FFFFFFFFFF", "FLlF..FLlF"]  # spans both eyes: they are 6 columns apart


def accessory(c, kind):
    """The accessory's layers [(rows, x, y)] in body coordinates."""
    a = c["anchors"]
    if kind == "beanie":
        return [(BEANIE, a["hat_x"], a["head_top"] - 3)]
    if kind == "bow":
        return [(BOW, *a["bow"])]
    if kind == "shades":
        return [(SHADES, c["eyes"][0][0] - 1, a["eye_y"])]
    if kind == "scarf":
        x0, x1 = a["neck"]
        band = "".join("F" if (x // 2) % 2 == 0 else "f" for x in range(x0, x1 + 1))
        return [([band], x0, a["neck_y"]), (["FF", "Ff", "F."], x0 + 1, a["neck_y"] + 1)]
    if kind == "headphones":
        # The band hugs the head's outline, so it fits every character.
        art = c["art"]
        edge = lambda r: (len(art[r]) - len(art[r].lstrip(".")), len(art[r].rstrip(".")) - 1)
        top = a["head_top"]
        left, right = edge(top)
        layers = [(["f" * (right - left + 1)], left, top - 1)]
        for r in range(top, a["eye_y"]):
            left, right = edge(r)
            layers += [(["f"], left - 1, r), (["f"], right + 1, r)]
        left, right = edge(a["eye_y"])
        cup = ["FF", "FF", "FF"]
        return layers + [(cup, left - 2, a["eye_y"]), (cup, right + 1, a["eye_y"])]
    return []


# ---------------------------------------------------------------------------
# Small sprites for effects.

TOKEN = [".Y.", "YyY", ".Y."]
SPARKLE = ["..Y..", "..y..", "YyWyY", "..y..", "..Y.."]
BUBBLE = [
    ".KKKKK.",
    "KwwXwwK",
    "KwwXwwK",
    "KwwXwwK",
    "KwwwwwK",
    "KwwXwwK",
    ".KKKKK.",
    "...K...",
]
Z_SMALL = ["ZZZ", "..Z", ".Z.", "Z..", "ZZZ"]
Z_BIG = ["ZZZZ", "...Z", "..Z.", ".Z..", "ZZZZ"]


def check(name, rows, width=18, height=17):
    assert len(rows) == height, f"{name}: {len(rows)} rows"
    for i, r in enumerate(rows):
        assert len(r) == width, f"{name} row {i}: {len(r)} cols: {r!r}"


def paint(canvas, rows, x, y):
    """Paints rows of letters onto the canvas dict; '.' leaves it alone."""
    for dy, row in enumerate(rows):
        for dx, ch in enumerate(row):
            if ch != "." and 0 <= x + dx < W and 0 <= y + dy < H:
                canvas[(x + dx, y + dy)] = ch


def body(c, eyes="open", mouth="smile"):
    rows = [list(r) for r in c["art"]]

    def patch(p, px, py):
        for dy, line in enumerate(p):
            for dx, ch in enumerate(line):
                rows[py + dy][px + dx] = ch

    if eyes == "shut":
        for ex, ey in c["eyes"]:
            patch(c["eye_shut"], ex, ey)
    mx, my = c["mouth"]
    patch(c["mouths"][mouth], mx, my)
    return ["".join(r) for r in rows]


def frame(c, eyes="open", mouth="smile", dx=0, dy=0, fx=(), acc="plain"):
    """One frame: the body and its accessory moved by (dx, dy), plus effects [(rows, x, y)]."""
    canvas = {}
    paint(canvas, body(c, eyes, mouth), BODY_X + dx, BODY_Y + dy)
    for rows, x, y in accessory(c, acc):
        paint(canvas, rows, BODY_X + dx + x, BODY_Y + dy + y)
    for rows, x, y in fx:
        paint(canvas, rows, x, y)
    return canvas


def states(c, acc="plain"):
    def f(**kw):  # a frame of this character, wearing its accessory
        return frame(c, acc=acc, **kw)

    mx, my = c["mouth"]
    mouth_y = BODY_Y + my  # canvas row of the mouth's top
    mouth_right = BODY_X + mx + 4  # first column past the mouth

    # Working: tokens fly in and get eaten. Four frames per token.
    if c["tokens"] == "side":
        path = [(W - 3, mouth_y - 1), (W - 6, mouth_y - 1), (mouth_right + 1, mouth_y - 1)]
    elif c["tokens"] == "tentacle":
        low = BODY_Y + 13  # level with the tentacles
        path = [(W - 4, low), (BODY_X + 15, low - 3), (mouth_right + 1, mouth_y - 1)]
    else:
        sx = BODY_X + c["slot"]
        path = [(sx, 0), (sx, 2), (sx, 4)]
    working = [
        (f(mouth="smile", fx=[(TOKEN, *path[0])]), 140),
        (f(mouth="open", dy=-1, fx=[(TOKEN, *path[1])]), 140),
        (f(mouth="open", fx=[(TOKEN, *path[2])]), 140),
        (f(mouth="smile", dy=-1), 180),
    ]

    # Blocked: shakes side to side under a "!" bubble.
    bubble = (BUBBLE, BODY_X + 15, 0)
    blocked = [
        (f(mouth="gasp", dx=-1, fx=[bubble]), 110),
        (f(mouth="gasp", dx=1, fx=[bubble]), 110),
        (f(mouth="gasp", dx=-1, fx=[bubble]), 110),
        (f(mouth="gasp", dx=0, fx=[bubble]), 500),
    ]

    # Done: a happy jump with sparkles.
    done = [
        (f(eyes="shut", mouth="smile"), 160),
        (f(eyes="shut", mouth="open", dy=-3, fx=[(SPARKLE, 0, 1), (SPARKLE, W - 5, 4)]), 160),
        (f(eyes="shut", mouth="open", dy=-4, fx=[(SPARKLE, 1, 4), (SPARKLE, W - 6, 0)]), 160),
        (f(eyes="shut", mouth="smile", dy=-1), 160),
        (f(eyes="shut", mouth="smile"), 600),
    ]

    # Idle: asleep, breathing, a z drifting up.
    idle = [
        (f(eyes="shut", fx=[(Z_SMALL, W - 8, 4)]), 600),
        (f(eyes="shut", dy=1, fx=[(Z_SMALL, W - 7, 2)]), 600),
        (f(eyes="shut", dy=1, fx=[(Z_BIG, W - 6, 0)]), 600),
        (f(eyes="shut", fx=[(Z_BIG, W - 6, 0)]), 600),
    ]
    return {"working": working, "blocked": blocked, "done": done, "idle": idle}


def hex_rgb(h):
    return tuple(int(h[i : i + 2], 16) for i in (1, 3, 5))


def save_gif(path, frames, colors):
    """Writes frames as a transparent, looping GIF. Palette index 0 is clear."""
    letters = sorted({ch for canvas, _ in frames for ch in canvas.values()})
    index = {ch: i + 1 for i, ch in enumerate(letters)}
    palette = [0, 0, 0]
    for ch in letters:
        palette += hex_rgb(colors[ch])
    images = []
    for canvas, _ in frames:
        im = Image.new("P", (W, H), 0)
        im.putpalette(palette)
        im.putdata([index[canvas[(x, y)]] if (x, y) in canvas else 0 for y in range(H) for x in range(W)])
        images.append(im.resize((W * SCALE, H * SCALE), Image.NEAREST))
    images[0].save(
        path,
        save_all=True,
        append_images=images[1:],
        duration=[ms for _, ms in frames],
        loop=0,
        transparency=0,
        disposal=2,
        optimize=False,
    )


# ---------------------------------------------------------------------------
# Habitats: the little scene behind each character on its card. One per
# character, in a day and a night version (night is shown while it sleeps).
# They are drawn with rectangles instead of letter grids: a scene is mostly
# big flat areas.

HW, HH = 40, 32  # habitat size, in art pixels
GROUND = 29  # first ground row; the avatar's feet stand on it


class Scene:
    def __init__(self):
        self.im = Image.new("RGBA", (HW, HH), (0, 0, 0, 0))

    def rect(self, x, y, w, h, color):
        rgb = hex_rgb(color)
        for yy in range(max(y, 0), min(y + h, HH)):
            for xx in range(max(x, 0), min(x + w, HW)):
                self.im.putpixel((xx, yy), rgb + (255,))

    def dot(self, x, y, color):
        self.rect(x, y, 1, 1, color)

    def bands(self, colors, y0=0, y1=GROUND):
        """Horizontal color bands from top to bottom: a pixel-art gradient."""
        step = (y1 - y0) / len(colors)
        for i, c in enumerate(colors):
            self.rect(0, y0 + round(i * step), HW, round(step) + 1, c)

    def save(self, path):
        self.im.resize((HW * SCALE, HH * SCALE), Image.NEAREST).save(path)


STARS = [(3, 3), (11, 6), (17, 2), (25, 8), (31, 4), (36, 10), (7, 11), (22, 13)]


def garden(night):
    s = Scene()
    if night:
        s.bands(["#141634", "#1b1e44", "#232857", "#2c3266"])
        for x, y in STARS:
            s.dot(x, y, "#e9e6ff")
        s.rect(31, 3, 4, 4, "#f4efd0")  # moon
        s.rect(33, 3, 2, 2, "#141634")  # crescent bite
        hill, hill2, grass, grass2 = "#24394a", "#1d3040", "#2c5a43", "#244a37"
    else:
        s.bands(["#7fc8f8", "#97d4f8", "#b2e0f7", "#cdeaf2"])
        s.rect(31, 3, 5, 5, "#ffe27a")  # sun
        s.rect(30, 4, 7, 3, "#ffe27a")
        s.rect(5, 5, 8, 2, "#ffffff")  # clouds
        s.rect(7, 4, 4, 1, "#ffffff")
        s.rect(18, 9, 6, 2, "#ffffff")
        hill, hill2, grass, grass2 = "#7cc58a", "#5fae74", "#4fa35f", "#3f8a4f"
    s.rect(0, 20, 16, 9, hill2)  # hills behind
    s.rect(3, 18, 10, 2, hill2)
    s.rect(22, 21, 18, 8, hill)
    s.rect(25, 19, 12, 2, hill)
    s.rect(0, GROUND, HW, HH - GROUND, grass)
    s.rect(0, GROUND, HW, 1, grass2)
    flowers = ["#ff8fa3", "#ffd34d", "#cdbdfb"] if not night else ["#7a5f8f", "#8f7a4f", "#5f5a8f"]
    for i, x in enumerate([2, 9, 30, 36]):
        s.dot(x, GROUND - 1, flowers[i % 3])
        s.dot(x, GROUND, grass2)
    return s


def desk(night):
    s = Scene()
    wall, stripe = ("#2a2440", "#30294a") if night else ("#e9d8b8", "#e1cca6")
    s.rect(0, 0, HW, GROUND, wall)
    for x in range(0, HW, 4):  # wallpaper stripes
        s.rect(x, 0, 2, GROUND, stripe)
    # Window, top right.
    s.rect(26, 3, 12, 10, "#5a4a3a")
    sky = "#121a3a" if night else "#8fd0f5"
    s.rect(27, 4, 10, 8, sky)
    s.rect(31, 4, 1, 8, "#5a4a3a")
    s.rect(27, 7, 10, 1, "#5a4a3a")
    if night:
        s.dot(29, 5, "#e9e6ff")
        s.dot(34, 9, "#e9e6ff")
        s.rect(34, 5, 2, 2, "#f4efd0")
    else:
        s.rect(28, 9, 3, 1, "#ffffff")
    # Shelf with a plant and books, top left.
    s.rect(2, 10, 14, 1, "#7a5a3a")
    s.rect(3, 6, 2, 4, "#e05570")
    s.rect(5, 7, 2, 3, "#6cb6ff")
    s.rect(7, 5, 2, 5, "#ffd34d")
    s.rect(11, 8, 4, 2, "#b25a3c")  # pot
    s.rect(11, 5, 1, 3, "#4fa35f")
    s.rect(13, 4, 1, 4, "#4fa35f")
    s.rect(12, 6, 1, 2, "#7cc58a")
    if night:  # lamp glow
        s.rect(20, 14, 6, 1, "#ffd34d")
        s.rect(22, 15, 2, 6, "#5a4a3a")
        s.rect(19, 15, 8, 3, "#3a3350")
    # Desk top as the ground.
    s.rect(0, GROUND, HW, HH - GROUND, "#8a6040" if not night else "#4a3428")
    s.rect(0, GROUND, HW, 1, "#a67650" if not night else "#5e4432")
    return s


def cave(night):
    s = Scene()
    s.bands(["#1a1426", "#221a32", "#2a203e", "#33264a"] if not night else ["#0e0b16", "#130f1e", "#181326", "#1d172e"])
    rock, rock2 = ("#3e3058", "#4a3a68") if not night else ("#241c36", "#2c2242")
    # Rock walls and stalactites.
    s.rect(0, 0, HW, 3, rock)
    for x, h in [(4, 5), (9, 3), (15, 6), (24, 4), (30, 7), (36, 3)]:
        s.rect(x, 0, 2, h, rock2)
        s.rect(x + 1, h, 1, 1, rock2)
    s.rect(0, 0, 3, GROUND, rock)
    s.rect(HW - 3, 0, 3, GROUND, rock)
    # Glowing crystals.
    glow = "#7cf0e0" if not night else "#a58bf0"
    for x, y in [(3, 14), (35, 11), (34, 20)]:
        s.rect(x, y, 2, 4, glow)
        s.dot(x, y - 1, glow)
    # Treasure: a pile of coins on the right.
    for x, y, w in [(28, 27, 8), (30, 26, 5), (31, 25, 3)]:
        s.rect(x, y, w, 1, "#ffd34d")
    s.dot(32, 25, "#fff3b0")
    s.dot(29, 27, "#fff3b0")
    # Floor with a lava glow seam.
    s.rect(0, GROUND, HW, HH - GROUND, rock)
    s.rect(0, GROUND, HW, 1, rock2)
    s.rect(4, HH - 1, 8, 1, "#e8664f")
    s.rect(20, HH - 1, 6, 1, "#f2a24a")
    return s


def moonbase(night):
    s = Scene()
    if night:
        s.bands(["#07070f", "#0b0b18", "#10101f", "#151528"])
        for x, y in STARS + [(14, 8), (28, 12), (5, 15), (38, 2)]:
            s.dot(x, y, "#ffffff")
        earth, land = "#24456e", "#2f6448"
    else:
        s.bands(["#1a1f3d", "#222852", "#2b3266", "#353d78"])
        for x, y in STARS[:4]:
            s.dot(x, y, "#9aa0c8")
        earth, land = "#3f8ee0", "#5cc98a"
    # The Earth, top left: a pixel circle with two continents.
    s.rect(5, 3, 6, 8, earth)
    s.rect(4, 4, 8, 6, earth)
    s.rect(6, 5, 3, 2, land)
    s.rect(8, 8, 2, 1, land)
    if not night:
        s.dot(5, 5, "#ffffff")
        s.rect(9, 4, 2, 1, "#ffffff")
    # Lunar horizon and ground.
    dust, dust2, pit = ("#4a4a62", "#5a5a74", "#34344a") if night else ("#8a8aa4", "#a2a2bc", "#6c6c88")
    s.rect(0, 24, HW, GROUND - 24, dust2)
    s.rect(14, 22, 12, 2, dust2)
    s.rect(0, GROUND, HW, HH - GROUND, dust)
    s.rect(0, GROUND, HW, 1, dust2)
    for x, y, w in [(2, 26, 5), (19, 25, 4), (12, 30, 6), (30, 31, 5)]:  # craters
        s.rect(x, y, w, 1, pit)
        s.rect(x + 1, y + 1, w - 2, 1, pit)  # rect() clips at the bottom edge
    # The base, bottom right: a dome with a lit window and a blinking-red antenna.
    dome = "#5c6488" if night else "#cfd3e6"
    s.rect(30, 23, 9, 6, dome)
    s.rect(31, 22, 7, 1, dome)
    s.rect(32, 21, 5, 1, dome)
    s.rect(33, 25, 3, 2, "#ffd34d" if night else "#7cc7ff")
    s.rect(34, 15, 1, 6, "#a3adc9")
    s.dot(34, 14, "#ff5c74")
    # A little flag, far left.
    s.rect(1, 19, 1, 7, "#cfd3e6")
    s.rect(2, 19, 3, 2, "#ff8fa3" if not night else "#a0566a")
    return s


HABITATS = {"sparky": garden, "byte": desk, "ember": cave, "nova": moonbase}


def avatar_order():
    """Every avatar, most distinct first: all character x color pairs without
    an accessory, then the same pairs with each accessory."""
    order = []
    for acc in ACCESSORIES:
        for v in range(3):
            for name, c in CHARACTERS.items():
                variant = list(c["variants"])[v]
                order.append((name, variant, acc))
    return order


def main():
    for old in OUT.glob("*.gif"):  # drop files from names that no longer exist
        old.unlink()
    avatars = avatar_order()
    for name, variant, acc in avatars:
        c = CHARACTERS[name]
        check(name, c["art"])
        palette = {**BASE, **c["variants"][variant], **ACCESSORIES[acc]}
        for state, frames in states(c, acc).items():
            save_gif(OUT / f"{name}-{variant}-{acc}-{state}.gif", frames, palette)
    print(f"{len(avatars)} avatars, {len(avatars) * 4} gifs")
    # The mod reads the avatar list from here, so this file stays the one source.
    lines = ",\n".join(f'  {{ id: "{n}-{v}-{a}", character: "{n}", name: "{n.capitalize()}" }}' for n, v, a in avatars)
    # A look is a character in a color ("sparky-lilac"): a space gets one, and
    # each agent in it wears a different accessory on top of that look.
    looks = [f"{name}-{list(c['variants'])[v]}" for v in range(3) for name, c in CHARACTERS.items()]
    looks_js = ",\n".join(f'  "{look}"' for look in looks)
    accessories_js = ",\n".join(f'  "{acc}"' for acc in ACCESSORIES)
    (OUT / "avatars.js").write_text(
        "// Generated by generate.py. Do not edit.\n"
        f"export const AVATARS = [\n{lines},\n];\n"
        f"\n// Looks (character-color), most distinct first.\nexport const LOOKS = [\n{looks_js},\n];\n"
        f"\n// Accessories, in the order they are handed out.\nexport const ACCESSORIES = [\n{accessories_js},\n];\n"
    )
    for name, draw in HABITATS.items():
        for time in ("day", "night"):
            draw(time == "night").save(OUT / f"habitat-{name}-{time}.png")
            print(f"habitat-{name}-{time}.png")


if __name__ == "__main__":
    main()
