years_back_premise = 2
years_back_hypothesis = 6

# the hypothesis refers to the number of years back when John was thrice as old as Tom, which is also mentioned in the premise
if years_back_hypothesis != years_back_premise:
    # check if the number of years back in the hypothesis contradicts the number of years back reported in the premise
    label = "contradiction"
else:
    # if the number of years back in the hypothesis does not contradict the number of years back in the premise, we can infer entailment
    label = "entailment"

print(label)
