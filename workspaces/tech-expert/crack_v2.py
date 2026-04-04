import base64
import hashlib

ENCRYPTED_TEXT = """=YlW4]0xO:;Og8OBJ/[4fCP`:Loy(&<akg:K5'jx5}!STt:amb/9Rd$d6?nsl8J@
,Bo?tomED|d,kguNb)xon*8VUK;6xg(uYxvxWm6yKhC<h4mjO3L<9\Vy$*~.3,3D
(/SkhIWB}JY\~cVtz1T343G>$zM>EkK1@413{4XsMNalD\AFMd@UizJmCQ$}~SUn
3>`a@rbak$lCl`uB/8[1Sj*b@#j4u<n}@IF6wE.'y>1z1R2VQaX,NNMCS=f>WbFK
hxF~ZB}:#?^g=a/a.,6Yf'*-=c1u8=WMR7]okBM;on@ec!*Ez8I|V+F@Mp##+8$.
w;]<t)@q-+IeG$3Jj!^1P#8M$&QT3`ryyt#<P<Y)mrq7sp=nZkfBd)1d#XTI"'t$
LS;}Bib]oD.Gdv;Jg&|gF<&8@]v:(K,;KAl}B[Y9H-+Jo|@Ye1(aB}*.YN;YJ(U0
Zb%}Vhh`*+HTPWq+d>Q5!l"HHYPt@HsxJ9U~&]HHAM(%:C2~fg%hRe;L@V*y{&;u
nX%J7)4clJ(8kmc[<xJw/B]3l.:wug`?ql^<R63^0[Iyj"oo#V{h(Fj4P3e`)rxx
9alTK5~N'Ew*sh;3luRW,=3q%(vOME0\<U7>-2+{2G"^4@q0z$Y:!\,>5T+tTMLI"""
FULL_STR = ENCRYPTED_TEXT.replace('\n', '')

# 取得 App Store Binary 的 MD5 或部分內容作為 Key
app_path = "/System/Applications/App Store.app/Contents/MacOS/App Store"
try:
    with open(app_path, "rb") as f:
        binary_data = f.read()
    
    # 提示說是 binary 轉換成的十六進位編碼是 key
    # 考慮到字串長度，可能是 binary 的 MD5 或前 N 個 bytes 的 hex
    key_hex = binary_data[:32].hex() 
    print(f"提取 Key (Hex): {key_hex[:20]}...")

    # 模擬量子對稱解密，將 binary hex 融入解碼邏輯
    rows = [FULL_STR[i:i+64] for i in range(0, 640, 64)]
    out = []
    # 假設 key 會動態與每一段做交互 (如 XOR)
    key_bytes = bytes.fromhex(key_hex)
    for i in range(len(rows)):
        row = rows[i]
        # 解密邏輯：Row XOR Reverse(BinaryKey) XOR Symm
        decoded = "".join(chr(ord(row[j]) ^ key_bytes[j % len(key_bytes)]) for j in range(len(row)))
        out.append(decoded)
    
    print("\n--- 注入 App Store 核心 Key 後的解析片段 ---")
    print("".join(out)[:200])

except Exception as e:
    print(f"Error reading app store: {e}")
