walk_time_premise = 55
walk_time_hypothesis = 15

# the hypothesis talks about the time Darcy spends commuting to work by walking, which is also mentioned in the premise
if walk_time_hypothesis > walk_time_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif walk_time_hypothesis < walk_time_premise:
    # check if the hypothesis value entails the premise value
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
