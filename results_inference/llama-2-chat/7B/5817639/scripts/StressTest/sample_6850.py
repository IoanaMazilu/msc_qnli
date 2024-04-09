less_than_premise = 20
hypothesis_apples = 10

# check if the hypothesis value contradicts the premise value
if hypothesis_apples > less_than_premise:
    label = "contradiction"
elif hypothesis_apples == less_than_premise:
    # the hypothesis value matches the premise value, so we can infer entailment
    label = "entailment"
else:
    # the premise value is only an estimate, so we cannot conclude anything
    label = "neutral"

print(label)
