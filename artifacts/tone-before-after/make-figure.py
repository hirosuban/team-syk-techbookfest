"""Lay out matching crops of the supplied manuscript pages without retouching."""

import base64
import hashlib
import json
import struct
import subprocess
import sys
from pathlib import Path


ROOT = Path(__file__).resolve().parents[2]
DESKTOP = Path('/mnt/c/Users/gckai/OneDrive/Desktop')
SOURCES = [DESKTOP / 'コミック 20261112.png', DESKTOP / 'トーン検証用_見本原稿.png']
CROP = (1620, 1080, 1010, 1180)  # x, y, width, height in both original pages


def main():
    sources = list(map(Path, sys.argv[1:])) or SOURCES
    if len(sources) != 2:
        raise SystemExit('Usage: make-figure.py [LINE_ART.png TONED.png]')
    panels = []
    records = []
    for index, (source, label) in enumerate(zip(sources, ['線画', '髪にトーンを貼った後'])):
        data = source.read_bytes()
        if data[:8] != b'\x89PNG\r\n\x1a\n':
            raise ValueError(f'Expected PNG: {source}')
        width, height = struct.unpack('>II', data[16:24])
        if (width, height) != (4299, 6071):
            raise ValueError(f'Unexpected source dimensions: {source}: {width}x{height}')
        x = 24 + index * 500
        encoded = base64.b64encode(data).decode('ascii')
        panels.append(f'''  <text x="{x + 226}" y="42" text-anchor="middle" font-family="IPAGothic, sans-serif" font-size="26" fill="#222">{label}</text>
  <svg x="{x}" y="64" width="452" height="528" viewBox="{' '.join(map(str, CROP))}" overflow="hidden">
    <image width="{width}" height="{height}" xlink:href="data:image/png;base64,{encoded}"/>
  </svg>
  <rect x="{x}" y="64" width="452" height="528" fill="none" stroke="#777" stroke-width="1.5"/>''')
        records.append({'filename': source.name, 'sha256': hashlib.sha256(data).hexdigest(),
                        'size': [width, height], 'label': label})
    svg = ROOT / 'articles/images/kai/tone-before-after.svg'
    svg.write_text('''<svg xmlns="http://www.w3.org/2000/svg" xmlns:xlink="http://www.w3.org/1999/xlink" width="1000" height="616" viewBox="0 0 1000 616" role="img" aria-labelledby="title description">
  <title id="title">髪にトーンを貼る前と後</title>
  <desc id="description">作者の漫画原稿の同じ人物を同じ範囲で切り出した比較図。左は線画、右は髪に網点のトーンを貼った完成見本。</desc>
  <rect width="1000" height="616" fill="#fff"/>
''' + '\n'.join(panels) + '\n</svg>\n', encoding='utf-8')
    subprocess.run(['rsvg-convert', '--width', '2000', '--height', '1232', str(svg),
                    '-o', str(svg.with_suffix('.png'))], check=True)
    subprocess.run(['rsvg-convert', '--format', 'pdf', str(svg), '-o',
                    str(ROOT / 'articles/images/latex/kai/tone-before-after.pdf')], check=True)
    Path(__file__).with_name('provenance.json').write_text(json.dumps({
        'sources': records, 'crop_xywh': CROP, 'retouched': False,
        'layout': 'Matching crops, left: line art; right: finished reference.',
        'outputs': ['articles/images/kai/tone-before-after.svg',
                    'articles/images/kai/tone-before-after.png',
                    'articles/images/latex/kai/tone-before-after.pdf'],
    }, ensure_ascii=False, indent=2) + '\n', encoding='utf-8')


if __name__ == '__main__':
    main()
