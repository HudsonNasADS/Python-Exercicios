print('Vamos converter o valor em metro para cm e mm etc.')
m = float(input('Digite o valor em metros(m): '))
km = (m/1000)
hm = (m/100)
dam = (m/10)
dm = (m*10)
cm = (m*100)
mm = (m*1000)
print('''O valo de {}m corresponde a: 
{:.3f}km
{}hm
{}dam
{:.0f}dm
{:.0f}cm
{:.0f}mm.'''.format(m, km, hm,dam, dm, cm, mm))

