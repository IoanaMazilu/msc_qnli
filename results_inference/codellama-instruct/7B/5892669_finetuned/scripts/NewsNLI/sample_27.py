terrorists_premise = 700
terrorists_hypothesis = 700

# the hypothesis mentions the number of terrorists and their families who fled Syria for Turkey, which is also mentioned in the premise
if terrorists_hypothesis!= terrorists_premise:
    # check if the number of terrorists in the hypothesis contradicts the number of terrorists reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
