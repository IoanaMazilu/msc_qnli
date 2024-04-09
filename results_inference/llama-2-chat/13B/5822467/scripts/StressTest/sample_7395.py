town_r_to_b_premise = 60
town_r_to_b_hypothesis = 50

# the hypothesis refers to the speed at which Tom drives
if town_r_to_b_hypothesis > town_r_to_b_premise:
    # the hypothesis explicitly entails the premise
    label = "entailment"
elif town_r_to_b_premise == town_r_to_b_hypothesis:
    # the premise and hypothesis are equal, so there is no contradiction or entailment
    label = "neutral"
else:
    # the premise indicates a constant speed of 60 miles per hour, while the hypothesis mentions a speed greater than 50 miles per hour
    # this implies that the hypothesis contradicts the premise
    label = "contradiction"

print(label)
