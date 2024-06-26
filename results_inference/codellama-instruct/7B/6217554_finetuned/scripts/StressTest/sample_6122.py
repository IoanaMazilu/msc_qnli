returned_tshirts_premise = 4
returned_tshirts_hypothesis = 8

if returned_tshirts_hypothesis <= returned_tshirts_premise:
    label = "contradiction"
else:
    label = "neutral"

print(label)
