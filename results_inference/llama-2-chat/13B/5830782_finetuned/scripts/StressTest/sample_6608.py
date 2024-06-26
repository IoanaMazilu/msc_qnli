years_premise = 2
years_hypothesis = 6
interest_rate = 4

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if years_hypothesis!= years_premise:
    # check if the number of years in the hypothesis contradicts the number of years in the premise
    label = "contradiction"
else:
    # if the number of years in the hypothesis does not contradict the number of years in the premise, we can infer entailment
    label = "entailment"

print(label)
