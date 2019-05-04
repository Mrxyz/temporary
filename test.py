import re
str=r'^[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}@[a-zA-Z0-9_-]+(\.[a-zA-Z0-9_-]+){0,4}$'
str=r'^[a-zA-Z0-9_][^@]+@[^\.]+.*?[^@\.]$'
if re.match(str,'1111helasdasdlo.world@163qq.com'):
	print('OK')
else:
	print("not a mail")
	
