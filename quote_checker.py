import re
import os
import glob

def normalize(text):
    if not text:
        return ""
    text = re.sub(r'<[^>]+>', '', text)
    text = re.sub(r'\s+', ' ', text)
    text = text.replace('„', '"').replace('“', '"').replace('”', '"').replace('“', '"').replace('«', '"').replace('»', '"').replace('"', '')
    text = text.replace('—', '-').replace('–', '-')
    text = text.replace('▪', '').replace('□', '').replace('|', '')
    text = text.replace('[…]', '').replace('…', '')
    return text.strip().lower()

def get_quotes_from_html(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()
    
    quotes = []
    # Find all <blockquote>...</blockquote>
    blocks = re.findall(r'<blockquote>(.*?)</blockquote>', html, re.DOTALL)
    for block in blocks:
        # separate span class="orig" and others
        orig_spans = re.findall(r'<span class="orig[^>]*>(.*?)</span>', block, re.DOTALL)
        for span in orig_spans:
            for part in span.split('·'):
                q = normalize(part)
                if q: quotes.append((q, part))
        
        # English translation or original English text (not inside span)
        text_without_spans = re.sub(r'<span[^>]*>.*?</span>', '', block, flags=re.DOTALL)
        for part in text_without_spans.split('·'):
            q = normalize(part)
            if q: quotes.append((q, part))
            
    return quotes

def check_quotes(chapter_file, corpus_file_map):
    print(f"--- Checking {chapter_file} ---")
    quotes = get_quotes_from_html(chapter_file)
    for q, orig_text in quotes:
        if len(q) < 20: continue
        
        found = False
        for fpath, content in corpus_file_map.items():
            if 'fr-' in fpath:
                continue # Skip FR
            if q in content:
                found = True
                break
            
            # Substring matching
            words = q.split()
            if len(words) > 10:
                chunk = " ".join(words[:10])
                if chunk in content:
                    found = True
                    break
        
        if not found:
            print(f"NOT FOUND: {orig_text.strip()}")

corpus_files = glob.glob('/home/diablo/book12/corpus-orig/*.txt')
corpus_map = {}
for cf in corpus_files:
    with open(cf, 'r', encoding='utf-8') as f:
        corpus_map[cf] = normalize(f.read())

import sys
targets = sys.argv[1:] or ['/home/diablo/book12/chapters/02-founding-story.html','/home/diablo/book12/chapters/04-the-war.html','/home/diablo/book12/chapters/05-first-peoples.html']
for t in targets:
    check_quotes(t, corpus_map)
