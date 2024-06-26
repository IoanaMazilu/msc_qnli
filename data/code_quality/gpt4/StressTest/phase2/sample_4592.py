borrowed_years_premise = 4
borrowed_years_hypothesis = 5

# the hypothesis refers to the number of years Arun borrowed a sum, as stated in the premise
if borrowed_years_hypothesis != borrowed_years_premise:
    # since 'borrowed_years_hypothesis' is not equal to 'borrowed_years_premise', it contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
