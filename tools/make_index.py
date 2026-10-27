import sys,os,re
src=open(sys.argv[1],encoding='utf-8').read()
head='<!doctype html>\n<html lang="ru">\n<head>\n<meta charset="utf-8">\n<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">\n'
i=src.index('</style>')+len('</style>')
out=head+src[:i]+'\n</head>\n<body>\n'+src[i:]+'\n</body>\n</html>\n'
# keep the author's own edits to the Capital G lyric line in the existing index.html
if os.path.exists(sys.argv[2]):
    old=open(sys.argv[2],encoding='utf-8').read()
    pat=re.compile(r'^[ \t]*<p class="lyr-ln.*$',re.M)
    mo,mn=pat.search(old),pat.search(out)
    if mo and mn: out=out[:mn.start()]+mo.group(0)+out[mn.end():]
open(sys.argv[2],'w',encoding='utf-8').write(out)
