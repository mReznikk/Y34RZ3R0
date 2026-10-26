import sys
src=open(sys.argv[1],encoding='utf-8').read()
head='<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
i=src.index('</style>')+len('</style>')
out=head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n'
open(sys.argv[2],'w',encoding='utf-8').write(out)
