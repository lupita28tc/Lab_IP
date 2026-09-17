Edad=17
tiene_credencial= True
tiene_adeudo= False

if Edad >= 18:
  es_mayor = True
else:
    es_mayor = False
documento_valido = tiene_credencial
if not tiene_adeudo:
    sin_adeudo = True
else:
    sin_adeudo = False
if es_mayor and documento_valido and sin_adeudo:
    autorizado = True
else:
    autorizado = False
print(autorizado)