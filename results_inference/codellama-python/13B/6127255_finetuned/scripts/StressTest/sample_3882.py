jogging_walking_time_premise = 3
jogging_walking_time_hypothesis = 4

# the hypothesis refers to the total time Aaron spends jogging and walking, which is also mentioned in the premise
if jogging_walking_time_hypothesis <= jogging_walking_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif jogging_walking_time_hypothesis > jogging_walking_time_premise:
    # check if the hypothesis value is greater than the premise value
    label = "entailment"
else:
    # if the hypothesis value does not contradict or is not greater than the premise value, we infer neutrality
    label = "neutral"

print(label)
