distance_walked_premise = 20
distance_walked_hypothesis = 80

# The hypothesis refers to the distance Sourav walked towards North, mentioned also in the premise
if distance_walked_premise >= distance_walked_hypothesis:
    # check if the distance walked in the premise contradicts the statement "less than 80 meters" in the hypothesis
    label = "contradiction"
elif distance_walked_premise != distance_walked_hypothesis:
    # If the distance walked in the premise is less than the distance mentioned in the hypothesis
    # it does not contradict the hypothesis, but cannot be explicitly entailed from it either
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise and can be explicitly entailed from it
    label = "entailment"

print(label)
