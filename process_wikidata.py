'''
分割されたwikidataファイルに対して、日本語の記述を抽出・必要な属性のみ格納するスクリプト
GNU parallel 等によるマルチコア実行を念頭においた:
 - ls /workspace/wikidata/split/latest-split-*.json.gz|parallel -j 18 "python process_wikidata.py {}"
TODO: alias情報の格納
'''
import gzip
import json
import jsonlines
from pathlib import Path
import time
import sys

assert len(sys.argv) == 2
filepath = Path(sys.argv[1])

start_time = time.time()

p = Path('/workspace/wikidata/processed')
outpath = p / f"output-{filepath.stem.split('.')[0]}.jsonl"
# 67,719,431

cnt = 0
lines = []
with gzip.open(filepath, 'rt') as fp:
    writer = jsonlines.open(outpath, mode='a')
    for l in fp:
        if len(l.strip()[:-1]) < 3:
            continue
        d = json.loads(l[:-2])
        if 'ja' in d['labels']:
            cnt += 1
            d_ja = {
                'id': d['id'],
                'title_ja': d['labels']['ja'],
                'title_en': d['labels'].get('en', None),
                'descriptions_ja': d['descriptions'].get('ja', None),
                'descriptions_en': d['descriptions'].get('en', None),
                'aliases_ja': [],
                'properties': d['claims']
            }
            aliases = d['aliases'].get('ja', None)
            if aliases is not None:
                aliases = [a['value'] for a in aliases]
                d_ja['aliases_ja'] = aliases
            lines.append(json.dumps(d_ja, ensure_ascii=False))
            if cnt % 100000 == 0:
                writer.write_all(lines)
                lines = []
                print(cnt)
if lines:
    writer.write_all(lines)
writer.close()
with open(outpath, encoding='utf8') as fp, \
     gzip.open(str(outpath) + '.gz', 'wt') as ofp:
    ofp.write(fp.read())

elapsed_time = time.time() - start_time
print(elapsed_time)
