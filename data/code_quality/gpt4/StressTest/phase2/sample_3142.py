years_premise = 22
years_hypothesis = 12

# the hypothesis refers to the same situation as the premise, but the number of years is less
if years_hypothesis >= years_premise:
    # check if the years in the hypothesis contradict the premise
    label = "contradiction"
else:
    # if the hypothesis years do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)