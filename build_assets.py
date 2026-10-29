#!/usr/bin/env python3
"""
Gera os SVGs do README (banner, cards de texto, títulos pixel, conectar, skills).
Uso:  python scripts/build_assets.py
Edite a seção CONFIG abaixo, rode o script e faça commit da pasta assets/.
Só usa a biblioteca padrão do Python.
"""
import json, random, textwrap, unicodedata
from pathlib import Path
from xml.sax.saxutils import escape

ROOT = Path(__file__).resolve().parent.parent
ASSETS = ROOT / "assets"
ASSETS.mkdir(exist_ok=True)
ICONS = json.loads((Path(__file__).parent / "icons.json").read_text())

# ───────────────────────────── CONFIG ─────────────────────────────
NAME = "LUÍS OTÁVIO GUERO"
SUBTITLE = "ENGENHARIA AEROESPACIAL / PYTHON & EMBEDDED"

# Cards de texto (um painel só, igual ao da imagem de referência)
ABOUT = [
    ("QUEM SOU",
     "Oi, eu sou o Luís Otávio, estudante de Engenharia Aeroespacial na UFSM, em Santa Maria (RS). "
     "Desenvolvo em Python e sistemas embarcados e gosto de ver projeto sair do papel, de um CubeSat "
     "lançado em foguete sub-orbital a automações com IA rodando em produção."),
    ("O QUE FAÇO",
     "Escrevo software em Python e C++, backends com FastAPI, integrações com LLMs e firmware para "
     "hardware embarcado. No dia a dia atuo como suporte técnico N3 em ERP fiscal, resolvendo problemas "
     "críticos de banco de dados (Firebird, PostgreSQL, MySQL)."),
    ("VISÃO",
     "Usar engenharia e software para resolver problemas reais, do espaço ao atendimento ao cliente. "
     "Aprender na prática, construir rápido e entregar de verdade."),
    ("ALÉM DO CÓDIGO",
     "Foguetes, satélites e qualquer coisa que dê para montar e testar na bancada."),
]

# Botões de contato (slug do ícone, rótulo, arquivo de saída)
CONNECT = [
    ("linkedin", "LINKEDIN"),
    ("github",   "GITHUB"),
    ("gmail",    "GMAIL"),
    # ("x", "X (TWITTER)"), ("medium", "MEDIUM"), ("kaggle", "KAGGLE"),
]

# Skills: (slug, rótulo). Slugs sem ícone na biblioteca caem para iniciais.
SKILLS = [
    ("python", "Python"), ("cplusplus", "C++"), ("c", "C"), ("typescript", "TypeScript"),
    ("javascript", "JavaScript"), ("postgresql", "PostgreSQL"), ("mysql", "MySQL"), ("mongodb", "MongoDB"),
    ("microsoftsqlserver", "SQL Server"), ("firebird", "Firebird"), ("fastapi", "FastAPI"), ("nodedotjs", "Node.js"),
    ("openai", "OpenAI"), ("react", "React"), ("tailwindcss", "Tailwind"), ("vite", "Vite"),
    ("arduino", "Arduino"), ("nvidia", "NVIDIA"), ("googlecolab", "Colab"), ("huggingface", "HuggingFace"),
    ("playwright", "Playwright"), ("docker", "Docker"), ("git", "Git"), ("figma", "Figma"),
]
FALLBACK = {  # iniciais + cor para quem não tem ícone
    "microsoftsqlserver": ("SQL", "CC2927"),
    "firebird": ("FB", "EF3939"),
    "playwright": ("PW", "2EAD33"),
}

# Títulos pixel avulsos (arquivo -> texto)
HEADERS = {
    "h-skills": "HABILIDADES",
    "h-activity": "ATIVIDADE RECENTE",
    "h-experience": "EXPERIÊNCIA",
    "h-projects": "PROJETOS",
    "h-awards": "PREMIAÇÕES",
}
# ───────────────────────────────────────────────────────────────────

W = 880
BG, BORDER = "#1c1c1c", "#333333"
TEXT = "#cfcfcf"
MONO = "ui-monospace, SFMono-Regular, Menlo, Consolas, 'Liberation Mono', 'DejaVu Sans Mono', monospace"
GREENS = ["#1f5a1a", "#2c7a24", "#3f9a35", "#58b345", "#7ccc58", "#a5de7a"]
CREAM, BLUE, ORANGE = "#e8e0cf", "#8fc4e8", "#e0702a"

# ── fonte pixel 5x7 ──
F = {}
def g(ch, rows): F[ch] = rows.split()
g("A","01110 10001 10001 11111 10001 10001 10001"); g("B","11110 10001 10001 11110 10001 10001 11110")
g("C","01110 10001 10000 10000 10000 10001 01110"); g("D","11110 10001 10001 10001 10001 10001 11110")
g("E","11111 10000 10000 11110 10000 10000 11111"); g("F","11111 10000 10000 11110 10000 10000 10000")
g("G","01110 10001 10000 10111 10001 10001 01111"); g("H","10001 10001 10001 11111 10001 10001 10001")
g("I","01110 00100 00100 00100 00100 00100 01110"); g("J","00111 00010 00010 00010 00010 10010 01100")
g("K","10001 10010 10100 11000 10100 10010 10001"); g("L","10000 10000 10000 10000 10000 10000 11111")
g("M","10001 11011 10101 10101 10001 10001 10001"); g("N","10001 11001 10101 10011 10001 10001 10001")
g("O","01110 10001 10001 10001 10001 10001 01110"); g("P","11110 10001 10001 11110 10000 10000 10000")
g("Q","01110 10001 10001 10001 10101 10010 01101"); g("R","11110 10001 10001 11110 10100 10010 10001")
g("S","01111 10000 10000 01110 00001 00001 11110"); g("T","11111 00100 00100 00100 00100 00100 00100")
g("U","10001 10001 10001 10001 10001 10001 01110"); g("V","10001 10001 10001 10001 10001 01010 00100")
g("W","10001 10001 10001 10101 10101 11011 10001"); g("X","10001 10001 01010 00100 01010 10001 10001")
g("Y","10001 10001 01010 00100 00100 00100 00100"); g("Z","11111 00001 00010 00100 01000 10000 11111")
g("0","01110 10001 10011 10101 11001 10001 01110"); g("1","00100 01100 00100 00100 00100 00100 01110")
g("2","01110 10001 00001 00010 00100 01000 11111"); g("3","11110 00001 00001 01110 00001 00001 11110")
g("4","00010 00110 01010 10010 11111 00010 00010"); g("5","11111 10000 11110 00001 00001 10001 01110")
g("6","00110 01000 10000 11110 10001 10001 01110"); g("7","11111 00001 00010 00100 01000 01000 01000")
g("8","01110 10001 10001 01110 10001 10001 01110"); g("9","01110 10001 10001 01111 00001 00010 01100")
g(" ","00000 00000 00000 00000 00000 00000 00000"); g("&","01100 10010 10100 01000 10101 10010 01101")
g("/","00001 00001 00010 00100 01000 10000 10000"); g("-","00000 00000 00000 11111 00000 00000 00000")
g(".","00000 00000 00000 00000 00000 01100 01100"); g("+","00000 00100 00100 11111 00100 00100 00000")
ACCENT = {"\u0301": ["00010", "00100"], "\u0300": ["01000", "00100"],
          "\u0302": ["00100", "01010"], "\u0303": ["01010", "10100"]}
CEDILLA = "\u0327"

def bitmap(text):
    """Texto -> matriz de linhas (2 de acento + 7 + 1 de cedilha)."""
    grid = [[] for _ in range(10)]
    for ch in text.upper():
        d = unicodedata.normalize("NFD", ch)
        base, marks = d[0], d[1:]
        glyph = F.get(base, F[" "])
        cols = [[0]*10 for _ in range(5)]
        for r, row in enumerate(glyph):
            for c, v in enumerate(row):
                if v == "1": cols[c][2 + r] = 1
        for m in marks:
            if m in ACCENT:
                for r, row in enumerate(ACCENT[m]):
                    for c, v in enumerate(row):
                        if v == "1": cols[c][r] = 1
            elif m == CEDILLA:
                cols[2][9] = 1
        for c in range(5):
            for r in range(10): grid[r].append(cols[c][r])
        for r in range(10): grid[r].append(0)   # espaço entre letras
    return grid

def pixel_path(text, x, y, px, color):
    grid = bitmap(text)
    d = []
    for r, row in enumerate(grid):
        c = 0
        while c < len(row):
            if row[c]:
                s = c
                while c < len(row) and row[c]: c += 1
                d.append(f"M{x+s*px} {y+r*px}h{(c-s)*px}v{px}h-{(c-s)*px}z")
            else: c += 1
    width = len(grid[0]) * px
    return f'<path d="{"".join(d)}" fill="{color}" shape-rendering="crispEdges"/>', width

def strip(x, y, w, px, seed, rows=2):
    """Faixa de pixels coloridos (decoração dos títulos), mais densa à direita."""
    rnd = random.Random(seed)
    cols = int(w // px)
    out = []
    for r in range(rows):
        c = 0
        while c < cols:
            p = (c / cols) ** 1.4 * 0.95
            span = rnd.choice([1, 1, 2, 3])
            if rnd.random() < p:
                u = rnd.random()
                col = (CREAM if u < .22 else BLUE if u < .40 else ORANGE if u < .44
                       else rnd.choice(GREENS))
                out.append(f'<rect x="{x+c*px}" y="{y+r*px}" width="{span*px}" height="{px}" fill="{col}"/>')
            c += span
    return "".join(out)

def svg(w, h, body):
    return (f'<svg xmlns="http://www.w3.org/2000/svg" width="{w}" height="{h}" viewBox="0 0 {w} {h}" '
            f'role="img">{body}</svg>')

def write(name, content):
    (ASSETS / name).write_text(content, encoding="utf-8")
    print("ok", name)

# ── banner ──
def banner():
    h, cell = 236, 14
    body = [f'<rect width="{W}" height="{h}" fill="{BG}"/>']
    name_svg, _ = pixel_path(NAME, 28, 22, 6, "#f2f2f2")
    body.append(name_svg)
    rnd = random.Random(42)
    cols, rows, y0 = W // cell + 1, 6, 112
    taken = set()
    for _ in range(22):                      # blocos creme, mais à direita
        c = int(cols * (0.35 + 0.65 * rnd.random() ** 0.8))
        r = rnd.randint(0, rows - 1)
        bw, bh = rnd.choice([(1, 1), (2, 1), (2, 2), (3, 2), (1, 2)])
        for dc in range(bw):
            for dr in range(bh):
                if r + dr < rows: taken.add((r + dr, c + dc))
    for r in range(rows):
        for c in range(cols):
            x, y = c * cell, y0 + r * cell
            if (r, c) in taken: col = CREAM
            else:
                edge = 0.15 if r in (0, rows - 1) else 0
                if rnd.random() < 0.03 + c / cols * 0.05: col = BLUE
                elif rnd.random() < 0.012: col = ORANGE
                elif rnd.random() < 0.10 + edge: continue
                else:
                    k = min(5, max(0, int(rnd.gauss(2.4 + 1.6 * (c / cols), 1.1))))
                    col = GREENS[k]
            body.append(f'<rect x="{x}" y="{y}" width="{cell}" height="{cell}" fill="{col}"/>')
    body.append(f'<text x="{W-28}" y="{h-18}" text-anchor="end" font-family="{MONO}" font-size="15" '
                f'letter-spacing="1" fill="#e0e0e0">{escape(SUBTITLE)}</text>')
    write("banner.svg", svg(W, h, '<g shape-rendering="crispEdges">' + "".join(body) + "</g>"))

# ── painel de texto (QUEM SOU / O QUE FAÇO / ...) ──
def about():
    pad, fs, lh = 28, 15, 22
    y, parts = 26, []
    for i, (title, text) in enumerate(ABOUT):
        t, tw = pixel_path(title, pad, y, 3, "#f2f2f2")
        parts.append(t)
        sx = pad + tw + 24
        parts.append(strip(sx, y + 18, W - pad - sx, 5, 100 + i))
        y += 30 + 24
        for line in textwrap.wrap(text, 86):
            parts.append(f'<text x="{pad}" y="{y}" font-family="{MONO}" font-size="{fs}" fill="{TEXT}">{escape(line)}</text>')
            y += lh
        y += 22
    h = y - 6
    body = f'<rect x=".5" y=".5" width="{W-1}" height="{h-1}" fill="{BG}" stroke="{BORDER}"/>' + "".join(parts)
    write("about.svg", svg(W, h, body))

# ── título pixel avulso ──
def header(name, text, seed):
    pad, h = 28, 60
    t, tw = pixel_path(text, pad, 14, 3, "#f2f2f2")
    sx = pad + tw + 24
    body = (f'<rect x=".5" y=".5" width="{W-1}" height="{h-1}" fill="{BG}" stroke="{BORDER}"/>' + t +
            strip(sx, 32, W - pad - sx, 5, seed))
    write(name + ".svg", svg(W, h, body))

# ── ícone (path simple-icons 24x24) ──
def icon_markup(slug, x, y, size):
    if slug in ICONS:
        ic = ICONS[slug]
        col = ic["hex"]
        lum = (int(col[0:2], 16) * .299 + int(col[2:4], 16) * .587 + int(col[4:6], 16) * .114) / 255
        fill = "#f0f0f0" if lum < 0.22 else "#" + col
        s = size / 24
        return f'<path transform="translate({x} {y}) scale({s})" d="{ic["path"]}" fill="{fill}"/>'
    txt, col = FALLBACK.get(slug, (slug[:2].upper(), "888888"))
    px = max(2, size // 14)
    t, tw = pixel_path(txt, 0, 0, px, "#" + col)
    ox = x + (size - tw) / 2
    return f'<g transform="translate({ox} {y + size/2 - 5*px})">{t}</g>'

def connect():
    w, h = 140, 118
    for slug, label in CONNECT:
        body = (f'<rect x=".5" y=".5" width="{w-1}" height="{h-1}" fill="#0f1a22" stroke="#1f3340"/>'
                f'<rect x=".5" y=".5" width="{w-1}" height="30" fill="#16232d" stroke="#1f3340"/>'
                f'<text x="{w/2}" y="20" text-anchor="middle" font-family="{MONO}" font-size="12" '
                f'font-weight="bold" fill="#e6e6e6">{escape(label)}</text>' +
                icon_markup(slug, w/2 - 21, 52, 42))
        write(f"connect-{slug}.svg", svg(w, h, body))

def skills():
    cols, cw, ch = 8, W // 8, 92
    rows = -(-len(SKILLS) // cols)
    h = rows * ch
    body = [f'<rect width="{W}" height="{h}" fill="#0f1a22"/>']
    for i, (slug, label) in enumerate(SKILLS):
        c, r = i % cols, i // cols
        x, y = c * cw, r * ch
        body.append(f'<rect x="{x+.5}" y="{y+.5}" width="{cw-1}" height="{ch-1}" fill="none" stroke="#1f3340"/>')
        body.append(icon_markup(slug, x + cw/2 - 18, y + 16, 36))
        body.append(f'<text x="{x+cw/2}" y="{y+ch-14}" text-anchor="middle" font-family="{MONO}" '
                    f'font-size="12" fill="#e6e6e6">{escape(label)}</text>')
    write("skills.svg", svg(W, h, "".join(body)))

if __name__ == "__main__":
    banner(); about(); connect(); skills()
    for i, (n, t) in enumerate(HEADERS.items()): header(n, t, 200 + i)
