premise_arrest_rate = 0.4
hypothesis_arrest_rate = 0.4

if hypothesis_arrest_rate!= premise_arrest_rate:
    label = "contradiction"
else:
    label = "entailment"

print(label)
