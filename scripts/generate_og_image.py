"""Generate GitHub social preview image (1280×640) for ma-case-study-pipeline.
Layout: title top → pipeline center → URL bottom."""
from PIL import Image, ImageDraw, ImageFont
import os

W, H = 1280, 640
BG = (13, 17, 23)
ACCENT = (88, 166, 255)
GREEN = (63, 185, 80)
ORANGE = (219, 109, 40)
PURPLE = (163, 113, 247)
WHITE = (230, 237, 243)
GRAY = (139, 148, 158)
DARK_GRAY = (33, 38, 45)
CARD_BG = (22, 27, 34)

img = Image.new('RGB', (W, H), BG)
draw = ImageDraw.Draw(img)

# ── Fonts ──
font_dir = r"C:\Windows\Fonts"
try:
 title_font = ImageFont.truetype(os.path.join(font_dir, "msyhbd.ttc"), 44)
 subtitle_font = ImageFont.truetype(os.path.join(font_dir, "msyh.ttc"), 25)
 mono_font = ImageFont.truetype(os.path.join(font_dir, "consola.ttf"), 17)
 small_font = ImageFont.truetype(os.path.join(font_dir, "msyh.ttc"), 15)
 tiny_font = ImageFont.truetype(os.path.join(font_dir, "msyh.ttc"), 12)
except Exception:
 title_font = subtitle_font = mono_font = small_font = tiny_font = ImageFont.load_default()

# ── Helper: centered text ──
def draw_centered(draw, text, y, font, fill):
 tw = draw.textlength(text, font=font)
 draw.text(((W - tw) / 2, y), text, fill=fill, font=font)

def draw_badge(draw, cx, y, text, fill, font):
 tw = int(draw.textlength(text, font=font) + 20)
 th = 28
 x = int(cx - tw / 2)
 draw.rounded_rectangle([x, y, x + tw, y + th], radius=4, fill=CARD_BG, outline=DARK_GRAY, width=1)
 draw.text((x + 10, y + 5), text, fill=fill, font=font)
 return tw

# ═══════════════════════════════════════
# TOP: title + stats
# ═══════════════════════════════════════

# Repo tag
tag = "ma-case-study-pipeline"
tag_w = int(draw.textlength(tag, font=mono_font) + 24)
draw.rounded_rectangle([(W - tag_w) // 2, 48, (W + tag_w) // 2, 76], radius=6, fill=CARD_BG, outline=DARK_GRAY, width=1)
draw.text(((W - draw.textlength(tag, font=mono_font)) / 2, 52), tag, fill=ACCENT, font=mono_font)

# Main title
draw_centered(draw, "M&A Case Study Pipeline", 100, title_font, WHITE)

# Subtitle
draw_centered(draw, "多模型学术生产流水线", 155, subtitle_font, GRAY)

# Stats badges (centered row)
stats = [("8 Stages", GREEN), ("5 Models", ACCENT), ("Blind Review", ORANGE), ("CC BY 4.0", GRAY)]
badge_spacing = 140
total_badges_w = (len(stats) - 1) * badge_spacing
start_x = (W - total_badges_w) // 2
for i, (text, color) in enumerate(stats):
 cx = start_x + i * badge_spacing
 draw_badge(draw, cx, 198, text, color, small_font)

# ═══════════════════════════════════════
# MIDDLE: pipeline P0→P8
# ═══════════════════════════════════════

PHASES = [
 ("P0", "选题否决", ACCENT),
 ("P1", "方案设计", (108, 170, 255)),
 ("P2", "领域审核", (121, 184, 255)),
 ("P3", "内容撰稿", (88, 166, 255)),
 ("P4", "总装质保", GREEN),
 ("P5", "交叉盲审", ORANGE),
 ("P6", "整合裁决", (235, 150, 70)),
 ("P7", "设计回溯", PURPLE),
 ("P8", "答辩模拟", (180, 140, 247)),
]

N = len(PHASES)
node_r = 30
gap = 40 # gap between nodes
total_w = N * node_r * 2 + (N - 1) * gap
pipe_x0 = (W - total_w) // 2
pipe_y = 290 # center of nodes

# Arrow line
arrow_y = pipe_y
draw.line([pipe_x0 + 2, arrow_y, pipe_x0 + total_w - 2, arrow_y], fill=DARK_GRAY, width=2)
# Arrow heads between nodes
for i in range(N - 1):
 ax = pipe_x0 + (i + 1) * (node_r * 2 + gap) - gap // 2
 draw.polygon([(ax, arrow_y), (ax - 8, arrow_y - 5), (ax - 8, arrow_y + 5)], fill=DARK_GRAY)

# Draw nodes
for i, (label, desc, color) in enumerate(PHASES):
 cx = pipe_x0 + node_r + i * (node_r * 2 + gap)
 cy = pipe_y

 # Glow ring
 for g in range(3):
 r = node_r + 3 + g * 2
 alpha = max(0, 35 - g * 11)
 glow = tuple(int(c * alpha / 255 + BG[j] * (1 - alpha / 255)) for j, c in enumerate(color))
 draw.ellipse([cx - r, cy - r, cx + r, cy + r], fill=glow)

 # Main circle
 draw.ellipse([cx - node_r, cy - node_r, cx + node_r, cy + node_r], fill=color)

 # Label inside
 lw = draw.textlength(label, font=small_font)
 draw.text((cx - lw / 2, cy - 8), label, fill=WHITE, font=small_font)

 # Description below
 dw = draw.textlength(desc, font=tiny_font)
 draw.text((cx - dw / 2, cy + node_r + 8), desc, fill=GRAY, font=tiny_font)

# ═══════════════════════════════════════
# BRIDGE: description + model tags
# ═══════════════════════════════════════

desc_lines = [
 "A multi-model collaborative pipeline that turns academic writing into a structured,",
 "auditable process — each phase has its own prompt + config, no model reviews its own work.",
]
dy = 380
for line in desc_lines:
 draw_centered(draw, line, dy, tiny_font, GRAY)
 dy += 20

# Model tags
models = [
 ("Kimi", (108, 170, 255)),
 ("GLM", (121, 184, 255)),
 ("GPT", (88, 166, 255)),
 ("Claude", GREEN),
 ("Qwen", ORANGE),
]
model_y = 430
total_mw = len(models) * 100
mx0 = (W - total_mw) // 2
for i, (name, color) in enumerate(models):
 cx = mx0 + i * 100 + 50
 tw = int(draw.textlength(name, font=small_font) + 24)
 th = 26
 x = int(cx - tw / 2)
 draw.rounded_rectangle([x, model_y, x + tw, model_y + th], radius=4, fill=CARD_BG, outline=DARK_GRAY, width=1)
 draw.text((x + 12, model_y + 4), name, fill=color, font=small_font)

# ═══════════════════════════════════════
# BOTTOM: URL + accent bar
# ═══════════════════════════════════════

# Subtle separator
sep_y = 495
draw.line([128, sep_y, W - 128, sep_y], fill=DARK_GRAY, width=1)

# URL
url = "github.com/redamancy231-create/ma-case-study-pipeline"
draw_centered(draw, url, 515, mono_font, GRAY)

# Tagline
draw_centered(draw, "Methodology Demo · CC BY 4.0 · 2026", 542, tiny_font, DARK_GRAY)

# Accent bottom bar
draw.rectangle([0, H - 3, W, H], fill=ACCENT)
for i in range(3):
 c = tuple(int(ACCENT[j] * (1 - i * 0.25)) for j in range(3))
 draw.rectangle([0, H - 7 - i, W, H - 3 - i], fill=c)

# ── Save ──
out_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "docs", "social-preview.png")
os.makedirs(os.path.dirname(out_path), exist_ok=True)
img.save(out_path, "PNG")
print(f"Saved: {out_path}")
print(f"Size: {W}×{H}")
