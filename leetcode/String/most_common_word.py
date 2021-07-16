### leetcode 819
## Most Common Word
# 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
# 대소문자 구분하지 않으며, 구두점(마침표, 쉼표 등) 또한 무시한다. 

import re
import collections

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]

words = [word for word in re.sub(r'[^A-Za-z]', " ",paragraph).lower().split() if word not in banned]

counts = collections.Counter(words)

print(counts.most_common(1)[0][0])
    
    

