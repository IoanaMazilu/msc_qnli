debentures_premise = 20000
debentures_hypothesis = 80000

# the hypothesis talks about the amount of money spent to buy debentures, referenced also in the premise
if debentures_premise > debentures_hypothesis:
    # check if the hypothesis value contradicts the amount of money spent in the premise
    label = "contradiction"
elif debentures_premise == debentures_hypothesis:
    # check if the hypothesis value is the same as the one in the premise
    label = "entailment"
else:
    # the premise gives only a specific amount for the debentures
    # any amount less than 'debentures_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
