jogging_time_premise = 3
jogging_time_hypothesis = 4

# the hypothesis refers to the total jogging time mentioned in the premise
if jogging_time_hypothesis <= jogging_time_premise:
    # check if the hypothesis value contradicts the estimate of 'jogging_time_premise'
    label = "contradiction"
elif jogging_time_hypothesis > jogging_time_premise:
    # check if the hypothesis value exceeds the premise one, which means it cannot be entailed
    label = "neutral"
else:
    # if the hypothesis value is less than or equal to the premise one, we can infer entailment
    label = "entailment"

print(label)
