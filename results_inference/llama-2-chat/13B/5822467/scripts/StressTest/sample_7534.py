leo_weight_premise = 50
leo_weight_hypothesis = 10
kendra_weight_premise = 50

# the hypothesis refers to the weight gain of Leo and the premise mentions the percentage increase
if leo_weight_hypothesis <= (kendra_weight_premise * 0.5):
    # check if the estimate of 'leo_weight_hypothesis' contradicts the percentage increase mentioned in the premise
    label = "contradiction"
else:
    # the premise gives a percentage increase, the hypothesis gives a specific weight gain
    # any weight gain greater than 'kendra_weight_premise * 0.5' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
