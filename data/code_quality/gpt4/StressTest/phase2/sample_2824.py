hamburgers_cost_premise = 66.50
hamburgers_cost_hypothesis = 66.50
hamburgers_count_premise = 30
hamburgers_count_hypothesis = 50

# the hypothesis refers to the same purchase Caleb made in the premise
if hamburgers_cost_premise != hamburgers_cost_hypothesis:
    # check if the cost of hamburgers in the hypothesis contradicts the cost of hamburgers mentioned in the premise
    label = "contradiction"
elif hamburgers_count_hypothesis <= hamburgers_count_premise:
    # check if the number of hamburgers in the hypothesis contradicts the estimate of more than 'hamburgers_count_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of hamburgers
    # any number of hamburgers greater than 'hamburgers_count_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
