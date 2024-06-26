premise_kg_butter = 44
hypothesis_kg_butter = 84

# the hypothesis refers to the quantity of butter mixed by Raman
if hypothesis_kg_butter >= premise_kg_butter:
    # check if the hypothesis value contradicts the quantity of butter mixed in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the quantity of butter mixed
    # any quantity of butter less than 'premise_kg_butter' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
