years_premise = 21
years_hypothesis = 71

# the hypothesis refers to the same situation as the premise, but in a different number of years
if years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the number of years in the hypothesis does not contradict the number of years in the premise, we can infer entailment
    label = "entailment"

print(label)
