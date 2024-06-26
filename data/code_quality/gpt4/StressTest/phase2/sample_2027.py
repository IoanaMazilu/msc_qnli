years_back_premise = 6
years_back_hypothesis = 6

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_back_hypothesis > years_back_premise:
    # check if the time frame of the hypothesis contradicts the time frame of the premise
    label = "contradiction"
elif years_back_hypothesis < years_back_premise:
    # check if the time frame of the hypothesis contradicts the time frame of the premise
    label = "contradiction"
else:
    # if the time frames match, we can infer entailment
    label = "entailment"

print(label)
