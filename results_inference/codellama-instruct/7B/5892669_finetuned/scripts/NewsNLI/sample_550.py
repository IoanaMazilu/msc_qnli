brightness_premise = 5
brightness_hypothesis = 5

# the hypothesis mentions the burned brightness of the meteor, which is also mentioned in the premise
if brightness_hypothesis!= brightness_premise:
    # check if the burned brightness in the hypothesis contradicts the burned brightness reported in the premise
    label = "contradiction"
else:
    # if the burned brightness in the hypothesis does not contradict the burned brightness in the premise, we can infer entailment
    label = "entailment"

print(label)
