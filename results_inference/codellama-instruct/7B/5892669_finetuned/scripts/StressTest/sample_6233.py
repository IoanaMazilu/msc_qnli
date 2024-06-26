cleaning_time_premise = 4
cleaning_time_hypothesis = 3

# the hypothesis refers to the cleaning time mentioned in the premise
if cleaning_time_hypothesis!= cleaning_time_premise:
    # check if the cleaning time in the hypothesis contradicts the cleaning time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)