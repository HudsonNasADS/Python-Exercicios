print('Vamos dizer se sua cidade começa com "Santo".')
cid = str(input('Digite o nome da sua  cidade: ')).strip().upper()
div = cid.split()
print('A cidade de {} tem a primeiro nome "SANTO"?: {} '.format(cid, "SANTO" in div[0]))
