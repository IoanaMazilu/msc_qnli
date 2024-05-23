cleaning_time_premise = 3
cleaning_time_hypothesis = 5

# the hypothesis refers to the cleaning time mentioned in the premise
if cleaning_time_premise > cleaning_time_hypothesis:
    # check if the 'cleaning_time_premise' contradicts the estimate of 'less than cleaning_time_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)