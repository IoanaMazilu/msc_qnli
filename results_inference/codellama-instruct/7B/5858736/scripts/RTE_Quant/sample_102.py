premise_mortar_attack = 4
premise_wounded = 80
premise_kidnapped = 1

hypothesis_mortar_attack = 4
hypothesis_wounded = 80

if hypothesis_mortar_attack!= premise_mortar_attack:
    label = "contradiction"
elif hypothesis_wounded!= premise_wounded:
    label = "contradiction"
else:
    label = "entailment"

print(label)
