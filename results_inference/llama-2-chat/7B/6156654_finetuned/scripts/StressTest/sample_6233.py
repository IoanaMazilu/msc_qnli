cleaning_time_premise = 4
cleaning_time_hypothesis = 3

# the hypothesis refers to the cleaning time of the house, which is also mentioned in the premise
if cleaning_time_hypothesis!= cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the cleaning time in the premise
    label = "contradiction"
else:
    # if the cleaning time in the hypothesis does not contradict the cleaning time in the premise, we can infer entailment
    label = "entailment"

print(label)
