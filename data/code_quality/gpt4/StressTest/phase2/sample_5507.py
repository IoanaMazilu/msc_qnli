debenture_premise = 10000
debenture_hypothesis = 40000

# the hypothesis refers to the amount of debentures Jaclyn bought, which is also mentioned in the premise
if debenture_hypothesis != debenture_premise:
    # check if the amount of debentures bought in the hypothesis contradicts the amount mentioned in the premise
    label = "contradiction"
else:
    # if the amount of debentures bought in the hypothesis does not contradict the amount in the premise, we can infer entailment
    label = "entailment"

print(label)
