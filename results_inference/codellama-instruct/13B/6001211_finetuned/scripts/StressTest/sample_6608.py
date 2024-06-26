years_premise = 2
years_hypothesis = 6
interest_rate = 4

# the hypothesis refers to the number of years and interest rate mentioned in the premise
if years_premise!= years_hypothesis:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
