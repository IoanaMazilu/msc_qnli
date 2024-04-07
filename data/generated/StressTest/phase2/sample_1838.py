# Premise: Caleb spends $68.50 on 50 hamburgers for the marching band.
# Hypothesis: Caleb spends $68.50 on more than 50 hamburgers for the marching band.
# Golden Label: contradiction

spend_premise = 68.50
hamburgers_premise = 50
spend_hypothesis = 68.50
hamburgers_hypothesis = 50

# the hypothesis refers to the amount spent and the number of hamburgers purchased mentioned in the premise
if spend_premise != spend_hypothesis:
    # check if the amount spent in hypothesis contradicts the amount spent in the premise
    label = "contradiction"
elif hamburgers_hypothesis > hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

