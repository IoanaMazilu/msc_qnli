distance_home_premise = 110
distance_home_hypothesis = 710

# the hypothesis talks about the same distance between Clarissa's work and home, mentioned in the premise
if distance_home_premise != distance_home_hypothesis:
    # check if the distance in the hypothesis contradicts the distance mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
