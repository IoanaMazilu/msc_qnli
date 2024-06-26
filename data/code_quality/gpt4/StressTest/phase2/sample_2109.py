spending_premise = 64.50
hamburgers_premise = 50
spending_hypothesis = 64.50
hamburgers_hypothesis = 80

# the hypothesis refers to the same spending and number of hamburgers mentioned in the premise
if spending_premise != spending_hypothesis:
    # check if the spending amount in the hypothesis contradicts the spending amount in the premise
    label = "contradiction"
elif hamburgers_hypothesis <= hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
