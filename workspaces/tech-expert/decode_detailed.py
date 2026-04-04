import base64

s = """=YlW4]0xO:;Og8OBJ/[4fCP`:Loy(&<akg:K5'jx5}!STt:amb/9Rd$d6?nsl8J@
,Bo?tomED|d,kguNb)xon*8VUK;6xg(uYxvxWm6yKhC<h4mjO3L<9\Vy$*~.3,3D
(/SkhIWB}JY\~cVtz1T343G>$zM>EkK1@413{4XsMNalD\AFMd@UizJmCQ$}~SUn
3>`a@rbak$lCl`uB/8[1Sj*b@#j4u<n}@IF6wE.'y>1z1R2VQaX,NNMCS=f>WbFK
hxF~ZB}:#?^g=a/a.,6Yf'*-=c1u8=WMR7]okBM;on@ec!*Ez8I|V+F@Mp##+8$.
w;]<t)@q-+IeG$3Jj!^1P#8M$&QT3`ryyt#<P<Y)mrq7sp=nZkfBd)1d#XTI"'t$
LS;}Bib]oD.Gdv;Jg&|gF<&8@]v:(K,;KAl}B[Y9H-+Jo|@Ye1(aB}*.YN;YJ(U0
Zb%}Vhh`*+HTPWq+d>Q5!l"HHYPt@HsxJ9U~&]HHAM(%:C2~fg%hRe;L@V*y{&;u
nX%J7)4clJ(8kmc[<xJw/B]3l.:wug`?ql^<R63^0[Iyj"oo#V{h(Fj4P3e`)rxx
9alTK5~N'Ew*sh;3luRW,=3q%(vOME0\<U7>-2+{2G"^4@q0z$Y:!\,>5T+tTMLI"""
s = s.replace('\n', '').strip()

print(f"Total length: {len(s)}")

# Try standard Base85 (RFC 1924)
try:
    print("\n--- Base85 (b85decode) ---")
    print(base64.b85decode(s).decode('utf-8', errors='ignore'))
except Exception as e:
    print(f"b85 error: {e}")

# Try standard Ascii85 (Adobe/Z85)
try:
    print("\n--- Ascii85 (a85decode) ---")
    print(base64.a85decode(s).decode('utf-8', errors='ignore'))
except Exception as e:
    print(f"a85 error: {e}")

# Caesar Cipher test for first few chars to see if it's just shifted text
print("\n--- Caesar Check ---")
for i in range(1, 26):
    shifted = "".join(chr((ord(c) - 65 - i) % 26 + 65) if c.isupper() else c for c in s[:20])
    if "http" in shifted.lower() or "task" in shifted.lower():
        print(f"Shift {i}: {shifted}")
