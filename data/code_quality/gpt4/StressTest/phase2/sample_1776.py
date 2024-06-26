spending_premise = 74.50
hamburgers_premise = 50
spending_hypothesis = 74.50
hamburgers_hypothesis = 10

# the hypothesis refers to the amount of money spent and hamburgers bought, mentioned also in the premise
if spending_premise != spending_hypothesis:
    # check if the amount of money spent in the hypothesis contradicts the amount spent in the premise
    label = "contradiction"
elif hamburgers_hypothesis >= hamburgers_premise:
    # check if the number of hamburgers in the hypothesis contradicts the number of hamburgers bought in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
