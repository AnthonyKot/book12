import re, glob

def normalize(text):
    return re.sub(r'\s+', ' ', text).strip()

def check_file_for_quotes(file_path):
    print(f"--- Processing {file_path} ---")
    with open(file_path, 'r', encoding='utf-8') as f:
        html = f.read()

    # Extract blockquotes
    quotes = re.findall(r'<span class="orig[^>]*>(.*?)</span>', html, re.DOTALL)
    quotes += re.findall(r'<blockquote>(.*?)<span class="cite">', html, re.DOTALL)
    
    # We just want to dump the quotes to inspect them and then we can check them in corpus
    for q in quotes:
        q_norm = normalize(re.sub(r'<[^>]+>', '', q))
        print("QUOTE:", q_norm)

check_file_for_quotes("/home/diablo/book12/chapters/02-founding-story.html")
