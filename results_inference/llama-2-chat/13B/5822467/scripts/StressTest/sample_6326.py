bobby_premise = 38
bonny_premise = 56
vijay_premise = 66
libin_premise = 75

bobby_hypothesis = 88
bonny_hypothesis = 56
vijay_hypothesis = 66
libin_hypothesis = 75

# check if the hypothesis values contradict the premise values
if bobby_hypothesis > bobby_premise:
    label = "contradiction"
elif bonny_hypothesis!= bonny_premise:
    label = "contradiction"
elif vijay_hypothesis!= vijay_premise:
    label = "contradiction"
elif libins_hypothesis!= libins_premise:
    label = "contradiction"
else:
    # if all hypothesis values are consistent with the premise values, we can infer entailment
    label = "entailment"

print(label)
