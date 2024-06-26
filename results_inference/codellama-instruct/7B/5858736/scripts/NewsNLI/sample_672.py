premise_snowfall_Urbana = 9
premise_snowfall_O'Hare = 3.9
hypothesis_snowfall_O'Hare = 3.9
hypothesis_snowfall_Detroit = 5.5

if hypothesis_snowfall_O'Hare!= premise_snowfall_O'Hare:
    label = "contradiction"
elif hypothesis_snowfall_Detroit!= premise_snowfall_O'Hare:
    label = "contradiction"
else:
    label = "entailment"

print(label)
