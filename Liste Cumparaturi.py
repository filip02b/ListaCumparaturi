def create_set(s):
    set_returned = set()
    for obj in s.split(','):
        set_returned.add(obj.strip())
    return set_returned

set_mama = create_set(input("Lista mamei: "))
set_ana = create_set(input("Lista anei: "))
set_maria = create_set(input("Lista mariei: "))

# set_cumparaturi = set_maria | set_ana # union

# # Ce mai e de cumparat
# set_rest_cumparaturi = set_mama - set_cumparaturi
# if set_rest_cumparaturi == set():
#     print("Nu mai este nimic de cumparat")
# else:
#     print("Mai avem de cumparat: ", set_rest_cumparaturi)

# # Ce s-a cumparat in plus
# set_cumparaturi_extra = set_cumparaturi - set_mama
# print("S-a cumparat in plus", set_cumparaturi_extra)

# # Cumparaturi duplicate
# cumparaturi_comune = set_ana.intersection(set_maria) #sau - folosim "&"
# if cumparaturi_comune == set():
#     print("Nu sunt cumparaturi duplicate")
# else:
#     print("Cumparaturi duplicate: ", cumparaturi_comune)

# # Ce a cumparat Anaa din lista mamei
# cumparaturi_comune_AnaMama = set_mama.intersection(set_ana)
# if cumparaturi_comune_AnaMama == set():
#     print("Ana nu a cumparat nimic din lista mamei")
# else:
#     print("Cumparaturile Anei din lista mamei: ", cumparaturi_comune_AnaMama)

# # Ce a cumparat Anaa in plus fata de lista mamei
# set_cumparaturi_extra_ana = set_ana - set_mama
# print("Ana a cumparat in plus", set_cumparaturi_extra_ana)

# Ce a cumparat Maria din lista mamei
cumparaturi_comune_MariaMama = set_mama.intersection(set_maria)
if cumparaturi_comune_MariaMama == set():
    print("Maria nu a cumparat nimic din lista mamei")
else:
    print("Cumparaturile Mariei din lista mamei: ", cumparaturi_comune_MariaMama)

# Ce a cumparat Maria in plus fata de lista mamei
set_cumparaturi_extra_maria = set_maria - set_mama
print("Ana a cumparat in plus", set_cumparaturi_extra_maria)
