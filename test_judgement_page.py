from pathlib import Path


page = Path("judgement.html").read_text(encoding="utf-8")

assert 'fetch("judgement-bank-300.json")' in page
assert 'ai-trainer-l3-judgement-v1' in page
assert '["√","×"]' in page
assert 'esc(q.note)' in page
assert 'id=removeWrongQuestion' in page
assert 'href="index.html"' in page
assert 'wrongRecords=JSON.parse' in page

main = Path("index.html").read_text(encoding="utf-8")
assert 'href="judgement.html"' in main

print("judgement page requirements satisfied")
