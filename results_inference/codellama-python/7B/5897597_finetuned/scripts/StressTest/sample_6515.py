john_age_past_premise = 6
john_age_past_hypothesis = 2

# the hypothesis refers to the age of John compared to Tom in the past, mentioned also in the premise
if john_age_past_hypothesis!= john_age_past_premise:
    # check if the age of John in the hypothesis contradicts the age of John in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
