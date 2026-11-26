import sys,re
BTN='''<!--back--><a href="./" class="xback" onclick="if(document.referrer&&history.length>1){history.back();return false}" style="position:fixed;left:max(12px,env(safe-area-inset-left,0px));bottom:calc(14px + env(safe-area-inset-bottom,0px));z-index:9999;display:inline-flex;align-items:center;gap:7px;padding:9px 13px;border-radius:999px;background:#1E1B18;color:#F9FAFA;font:500 12px/1 'IBM Plex Mono',ui-monospace,monospace;letter-spacing:.06em;text-transform:uppercase;text-decoration:none;box-shadow:0 2px 0 #000,0 8px 20px -8px rgba(0,0,0,.45)">&larr; All<span> versions</span></a><style>@media (max-width:480px){.xback span{display:none}}@media print{.xback{display:none!important}}</style><!--/back-->'''
for f in sys.argv[1:]:
    s=open(f).read()
    s=re.sub(r'<!--back-->.*?<!--/back-->','',s,flags=re.S)
    s=s.replace('</body>',BTN+'</body>',1) if '</body>' in s else s+BTN
    open(f,'w').write(s); print(f)
