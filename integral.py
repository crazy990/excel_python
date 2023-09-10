import sympy as sp

#kod kargaşasını önlemek için ayrı form larda kodlanıp projeye eklenecek.

def integral():
    #değişken değiştirme
    x,u =sp.symbols('x u')
    #integral fonksiyonu tanımlanması
    fonk = x**2
    # u fonksiyonu yani x e bağalacak değişken
    u_donusum = x**2

    sonuc = sp.integrate(fonk.subs(x,u_donusum)*sp.diff(u_donusum,x),(u,u_donusum))

    print("integralin sonucu : "+str(sonuc))

print(integral())


    