years_back_premise = 5
years_back_hypothesis = 6

# the hypothesis refers to the same situation as the premise, but with a different time frame
if years_back_hypothesis!= years_back_premise:
    # check if the time frame in the hypothesis contradicts the time frame mentioned in the premise
    label = "contradiction"
else:
    # if the time frame in the hypothesis does not contradict the time frame in the premise, we can infer entailment
    label = "entailment"

print(label)
