cleaning_time_premise = 3
cleaning_time_hypothesis = 5

# the hypothesis refers to the cleaning time if Anne's speed were doubled, which is also mentioned in the premise
if cleaning_time_premise > cleaning_time_hypothesis:
    # check if the cleaning time in the premise contradicts the estimate of less than 'cleaning_time_hypothesis'
    label = "contradiction"
elif cleaning_time_premise < cleaning_time_hypothesis:
    # if the cleaning time in the premise is less than the estimate in the hypothesis, we can infer entailment
    label = "entailment"
else:
    # if the cleaning times are equal, we can also infer entailment
    label = "entailment"

print(label)
