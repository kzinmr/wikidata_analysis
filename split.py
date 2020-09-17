'''
巨大な単一wikidataファイルを分割するスクリプト
'''
import gzip
from pathlib import Path
import time

start_time = time.time()

p = Path('/workspace/wikidata')

# 67,719,431

lines = []
with gzip.open(p / 'latest-all.json.gz', 'rt') as fp:
    writer = gzip.open(p / f'split/latest-split-00000000.json.gz', mode='at')
    for cnt, l in enumerate(fp, 1):
#        if cnt < 49000000:
#            continue
        lines.append(l)
        if cnt % 100000 == 0:
            print(cnt)
            writer.write(''.join(lines))
            lines = []
        if cnt % 1000000 == 0:
            writer.close()
            writer = gzip.open(p / f'split/latest-split-{cnt:08}.json.gz', mode='at')

if lines:
    with gzip.open(p / f'split/latest-split-{cnt:08}.json.gz', mode='wt') as writer:
        writer.write(''.join(lines))

elapsed_time = time.time() - start_time
print(elapsed_time)
