distance_to_walt_premise = 48
distance_to_walt_hypothesis = 58

# the hypothesis refers to the distance between Lionel's and Walt's house, mentioned in the premise
if distance_to_walt_hypothesis < distance_to_walt_premise:
    # check if the hypothesis value contradicts the exact distance mentioned in the premise
    label = "contradiction"
elif distance_to_walt_hypothesis > distance_to_walt_premise:
    # check if the hypothesis value is greater than the distance mentioned in the premise
    # in this case, the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise either
    label = "neutral"
else:
    # if the hypothesis value equals the premise one, we can infer entailment
    label = "entailment"

print(label)
