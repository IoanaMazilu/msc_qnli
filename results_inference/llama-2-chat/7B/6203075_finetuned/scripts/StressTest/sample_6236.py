cleaning_time_premise = 3
cleaning_time_hypothesis = 3

# the hypothesis refers to the cleaning time if Anne's speed was doubled, as mentioned in the premise
if cleaning_time_hypothesis!= cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the cleaning time reported in the premise
    label = "contradiction"
else:
    # if the cleaning time in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
