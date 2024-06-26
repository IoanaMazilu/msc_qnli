premise_kg_butter = 27
hypothesis_kg_butter = 77

# the hypothesis refers to the weight of butter mixed by Raman
if hypothesis_kg_butter <= premise_kg_butter:
    # check if the estimate of 'hypothesis_kg_butter' contradicts the weight of butter mixed in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the weight of butter mixed
    # any weight of butter greater than 'premise_kg_butter' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
