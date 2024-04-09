watermelons_premise = 136

# the hypothesis refers to the number of watermelons possessed by Mike after Sally left
less_than_136 = Hypothesis < 136

if less_than_136:
    # the hypothesis value contradicts the premise value
    label = "contradiction"
elif watermelons_premise == 136:
    # the premise and hypothesis values are equal
    label = "entailment"
else:
    # the premise gives a specific value, while the hypothesis gives a less specific value
    # the hypothesis value is not contradictory to the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
