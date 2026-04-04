import sys
from PIL import Image, ImageDraw, ImageFont, ImageOps
import os

def create_quote(image_path, text, name, date, output_path):
    # 1. 開啟圖片並轉黑白
    img = Image.open(image_path).convert('L')
    img = ImageOps.colorize(img, black="black", white="white") # 確保是標準黑白
    
    # 2. 調整大小 (縮放至寬度 1200)
    base_width = 1200
    w_percent = (base_width / float(img.size[0]))
    h_size = int((float(img.size[1]) * float(w_percent)))
    img = img.resize((base_width, h_size), Image.Resampling.LANCZOS)
    
    # 3. 繪製半透明遮罩與文字
    draw = ImageDraw.Draw(img)
    
    # 嘗試加載字型 (macOS 常用路徑)
    font_path = "/System/Library/Fonts/STHeiti Light.ttc" # 黑體
    if not os.path.exists(font_path):
        font_path = "/System/Library/Fonts/Cache/PingFang.ttc"
        
    title_font = ImageFont.truetype(font_path, 60)
    info_font = ImageFont.truetype(font_path, 30)
    
    # 在圖片下方加上漸層黑
    overlay = Image.new('RGBA', img.size, (0,0,0,0))
    draw_ov = ImageDraw.Draw(overlay)
    draw_ov.rectangle([0, h_size - 300, base_width, h_size], fill=(0,0,0,180))
    img = Image.alpha_composite(img.convert('RGBA'), overlay)
    
    # 重新取得 Draw 對象
    draw = ImageDraw.Draw(img)
    
    # 寫入文字 (簡單排版)
    draw.text((100, h_size - 220), f'"{text}"', font=title_font, fill="white")
    draw.text((100, h_size - 100), f"—— {name}", font=info_font, fill="white")
    draw.text((base_width - 250, h_size - 60), date, font=info_font, fill="#aaaaaa")
    
    img.convert('RGB').save(output_path)

if __name__ == "__main__":
    # args: image_path, text, name, date, output_path
    if len(sys.argv) >= 6:
        create_quote(sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5])
