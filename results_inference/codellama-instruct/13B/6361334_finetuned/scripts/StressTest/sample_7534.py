# define variables for the numerical entities in the premise and hypothesis
leo_gain_premise = 50
leo_gain_hypothesis = 10
kendra_weight_premise = 50
kendra_weight_hypothesis = 50

# check if the hypothesis value contradicts the premise estimate
if leo_gain_hypothesis > leo_gain_premise:
    label = "contradiction"
# check if the hypothesis value is consistent with the premise estimate
elif leo_gain_hypothesis <= leo_gain_premise:
    # check if the hypothesis value is consistent with the premise estimate
    if kendra_weight_hypothesis!= kendra_weight_premise:
        label = "contradiction"
    else:
        label = "entailment"
else:
    label = "neutral"

print(label)
