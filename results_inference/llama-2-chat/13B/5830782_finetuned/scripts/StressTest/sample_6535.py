miami_to_kennedy_premise = 7/3
miami_to_kennedy_hypothesis = 1/3
miami_to_logan_premise = 4
miami_to_logan_hypothesis = 4

# the hypothesis refers to the ratio of passengers between Miami and Kennedy and Miami and Logan airports
if miami_to_kennedy_hypothesis > miami_to_kennedy_premise:
    # check if the ratio of passengers between Miami and Kennedy in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
elif miami_to_logan_hypothesis!= miami_to_logan_premise:
    # check if the ratio of passengers between Miami and Logan in the hypothesis contradicts the ratio in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer neutrality
    label = "neutral"

print(label)
