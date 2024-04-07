# Premise: Caleb spends $68.50 on more than 20 hamburgers for the marching band.
# Hypothesis: Caleb spends $68.50 on 50 hamburgers for the marching band.
# Golden Label: neutral

spending_premise = 68.50
spending_hypothesis = 68.50
hamburger_count_premise = 20
hamburger_count_hypothesis = 50

# the hypothesis refers to the amount of money spent and the number of hamburgers mentioned in the premise
if spending_hypothesis != spending_premise:
    # check if the spending amount in the hypothesis contradicts the spending amount in the premise
    label = "contradiction"
elif hamburger_count_hypothesis <= hamburger_count_premise:
    # check if the number of hamburgers in the hypothesis contradicts the estimate of more than 'hamburger_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hamburgers
    # any number of hamburgers greater than 'hamburger_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

