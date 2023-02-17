usuário = {"nome": "Zé", "endereço": "Rua Aqui", "número": 1}
print("Pelas chaves")
for key in usuário.keys():
    print("\t", key)
print("Pelos valores")
for value in usuário.values():
    print("\t", value)
print("Os dois")
for key, value in usuário.items():
    print("\t", key, "com valor:", value)
