#PYTHONISTA
#DICTIONARY FROM CLIPBOARD FROM GOOGLE SHEET COPY

import clipboard
print(repr(clipboard.get()))

SOME=clipboard.get()
ALL=SOME.split('\n')
HEADER=ALL[0].split('\t')
#print(HEADER)
DICT=dict(zip(HEADER,[[] for DUMMY in range(len(HEADER))]))
#print(DICT)

for ONE in ALL:
#	print(repr(ONE))
	ONE=ONE.split('\t')
	print(ONE)
	for k, v in zip(HEADER, ONE):
		try:
			v=float(v)
		except:
			pass
		DICT[k].append(v)
print(DICT)

