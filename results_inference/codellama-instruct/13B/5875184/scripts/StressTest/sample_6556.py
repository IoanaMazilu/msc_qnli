premise_england_france = 0
premise_england_italy = 7
premise_france_italy = 11

hypothesis_england_france = 0
hypothesis_england_italy = 6
hypothesis_france_italy = 11

# check if the hypothesis values contradict the premise values
if hypothesis_england_france!= premise_england_france:
    label = "contradiction"
elif hypothesis_england_italy!= premise_england_italy:
    label = "contradiction"
elif hypothesis_france_italy!= premise_france_italy:
    label = "contradiction"
else:
    label = "entailment"

print(label)
