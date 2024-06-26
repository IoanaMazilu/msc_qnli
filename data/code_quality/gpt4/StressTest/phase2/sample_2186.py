years_premise = 4
years_hypothesis = 8

# the hypothesis refers to the same future period as the premise, but doubles it
if years_hypothesis != 2 * years_premise:
    # check if the number of years in the hypothesis contradicts the number of years mentioned in the premise
    label = "contradiction"
else:
    # if the number of years in the hypothesis does not contradict the one in the premise, we can infer entailment
    label = "entailment"

print(label)
