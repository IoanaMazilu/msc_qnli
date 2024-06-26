molly_max_speed_premise = 100
molly_max_speed_hypothesis = 100

# the hypothesis talks about the speed of Molly and Max, which is also mentioned in the premise
if molly_max_speed_premise > molly_max_speed_hypothesis:
    # check if the speed in the premise contradicts the speed in the hypothesis
    label = "contradiction"
elif molly_max_speed_premise == molly_max_speed_hypothesis:
    # if the speed in the premise equals the speed in the hypothesis, it's a neutral case
    label = "neutral"
else:
    # if the speed in the premise is less than the speed in the hypothesis, it's an entailment
    label = "entailment"

print(label)
