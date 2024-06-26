coin_amount_premise = 2
coin_amount_hypothesis = 3
coin_material_premise = "iron"
coin_material_hypothesis = "iron"

if coin_amount_hypothesis <= coin_amount_premise:
    label = "contradiction"
elif coin_material_hypothesis!= coin_material_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
