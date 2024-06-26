interest_premise = 200
interest_hypothesis = 200
years_premise = 2
years_hypothesis = 6

# the hypothesis refers to the amount of interest and the years of investment mentioned in the premise
if interest_premise != interest_hypothesis:
    # check if the interest in the hypothesis contradicts the interest reported in the premise
    label = "contradiction"
elif years_premise != years_hypothesis:
    # check if the years of investment in the hypothesis contradicts the years of investment reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
