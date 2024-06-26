amount_after_8_months_premise = 14000
amount_after_8_months_hypothesis = 14000

# the hypothesis refers to the amount John withdraws after 8 months, mentioned in the premise
if amount_after_8_months_hypothesis >= amount_after_8_months_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
