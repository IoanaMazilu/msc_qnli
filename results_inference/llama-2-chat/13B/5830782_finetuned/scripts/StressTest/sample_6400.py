miami_to_kennedy_premise = 8/2
miami_to_kennedy_hypothesis = 1/2
miami_to_logan_premise = 4
miami_to_logan_hypothesis = 4

# the hypothesis talks about the ratio of passengers between Miami, Kennedy and Logan airports, which is also mentioned in the premise
if miami_to_kennedy_hypothesis > miami_to_kennedy_premise:
    # check if the ratio of passengers between Miami and Kennedy contradicts the premise
    label = "contradiction"
elif miami_to_logan_hypothesis!= miami_to_logan_premise:
    # check if the ratio of passengers between Miami and Logan contradicts the premise
    label = "contradiction"
else:
    # the hypothesis values and ratios do not contradict the premise ones, but cannot be fully and explicitly entailed from the premise
    label = "neutral"

print(label)
