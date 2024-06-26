premise_compensatory_damages = 10000000
premise_punitive_damages = 50000000
hypothesis_total_damages = 60000000

if hypothesis_total_damages!= premise_compensatory_damages + premise_punitive_damages:
    label = "contradiction"
else:
    label = "entailment"

print(label)
