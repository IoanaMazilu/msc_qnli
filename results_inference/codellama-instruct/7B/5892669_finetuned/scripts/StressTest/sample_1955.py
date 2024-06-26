years_premise = 2
years_hypothesis = 2
interest_rate = 4

# the hypothesis refers to the number of years mentioned in the premise
if years_hypothesis >= years_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, we can infer entailment
    label = "entailment"

print(label)
