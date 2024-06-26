spend_premise = 70.50
hamburgers_premise = 50
spend_hypothesis = 70.50
hamburgers_hypothesis = 60

# the hypothesis refers to the amount spent and the number of hamburgers bought, mentioned in the premise
if spend_premise != spend_hypothesis:
    # check if the amount spent in the hypothesis contradicts the amount spent in the premise
    label = "contradiction"
elif hamburgers_premise >= hamburgers_hypothesis:
    # check if the number of hamburgers in the premise contradicts the estimate of less than 'hamburgers_hypothesis' in the hypothesis
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
