import base64

encrypted = """=YlW4]0xO:;Og8OBJ/[4fCP`:Loy(&<akg:K5'jx5}!STt:amb/9Rd$d6?nsl8J@
,Bo?tomED|d,kguNb)xon*8VUK;6xg(uYxvxWm6yKhC<h4mjO3L<9\Vy$*~.3,3D
(/SkhIWB}JY\~cVtz1T343G>$zM>EkK1@413{4XsMNalD\AFMd@UizJmCQ$}~SUn
3>`a@rbak$lCl`uB/8[1Sj*b@#j4u<n}@IF6wE.'y>1z1R2VQaX,NNMCS=f>WbFK
hxF~ZB}:#?^g=a/a.,6Yf'*-=c1u8=WMR7]okBM;on@ec!*Ez8I|V+F@Mp##+8$.
w;]<t)@q-+IeG$3Jj!^1P#8M$&QT3`ryyt#<P<Y)mrq7sp=nZkfBd)1d#XTI"'t$
LS;}Bib]oD.Gdv;Jg&|gF<&8@]v:(K,;KAl}B[Y9H-+Jo|@Ye1(aB}*.YN;YJ(U0
Zb%}Vhh`*+HTPWq+d>Q5!l"HHYPt@HsxJ9U~&]HHAM(%:C2~fg%hRe;L@V*y{&;u
nX%J7)4clJ(8kmc[<xJw/B]3l.:wug`?ql^<R63^0[Iyj"oo#V{h(Fj4P3e`)rxx
9alTK5~N'Ew*sh;3luRW,=3q%(vOME0\<U7>-2+{2G"^4@q0z$Y:!\,>5T+tTMLI"""
full = encrypted.replace('\n', '')

app_path = "/System/Applications/App Store.app/Contents/MacOS/App Store"
with open(app_path, "rb") as f:
    binary = f.read(1024)

# 嘗試不同長度的 Hex Key (提示說是 binary 轉換成的十六進位編碼)
# 可能是全內容、或者是前 16/32 位元組
potential_keys = [binary[:i].hex() for i in [16, 32, 64]]

for k_hex in potential_keys:
    k_bytes = bytes.fromhex(k_hex)
    # 嘗試對稱運算：(Char ^ Key_at_pos)
    try_str = "".join(chr(ord(full[i]) ^ k_bytes[i % len(k_bytes)]) for i in range(min(len(full), 128)))
    print(f"KeyLength {len(k_bytes)}: {try_str[:100]}...")

