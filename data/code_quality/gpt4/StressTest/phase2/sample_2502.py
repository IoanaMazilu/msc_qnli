distance_home_premise = 110
distance_home_hypothesis = 610

# the hypothesis talks about the distance that Clarissa drives home from work, referenced also in the premise
if distance_home_premise > distance_home_hypothesis:
    # check if the premise value contradicts the estimate of less than 'distance_home_hypothesis'
    label = "contradiction"
elif distance_home_premise != distance_home_hypothesis:
    # the hypothesis gives only an estimate for the distance
    # any distance less than 'distance_home_hypothesis' is consistent with the hypothesis, but cannot be explicitly entailed from the hypothesis
    label = "neutral"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
