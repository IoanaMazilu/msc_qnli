cleaning_time_premise = 3
cleaning_time_hypothesis = 3

# the hypothesis refers to the cleaning time if Anne's speed were doubled, also mentioned in the premise
if cleaning_time_hypothesis >= cleaning_time_premise:
    # check if the hypothesis value contradicts the premise value of 'cleaning_time_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
