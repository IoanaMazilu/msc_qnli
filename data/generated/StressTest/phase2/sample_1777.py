# Premise: Caleb spends $74.50 on more than 10 hamburgers for the marching band.
# Hypothesis: Caleb spends $74.50 on 50 hamburgers for the marching band.
# Golden Label: neutral

spend_premise = 74.50
hamburgers_premise = 10
spend_hypothesis = 74.50
hamburgers_hypothesis = 50

# the hypothesis refers to the total spend and number of hamburgers mentioned in the premise
if spend_hypothesis != spend_premise:
    # check if the hypothesis value contradicts the total spend in the premise
    label = "contradiction"
elif hamburgers_hypothesis <= hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the estimate of more than 'hamburgers_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hamburgers
    # any number of hamburgers greater than 'hamburgers_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

