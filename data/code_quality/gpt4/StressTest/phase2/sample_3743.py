spending_premise = 70.50
hamburgers_premise = 50
spending_hypothesis = 70.50
hamburgers_hypothesis = 50

# The hypothesis refers to the spending and number of hamburgers mentioned in the premise
if spending_hypothesis != spending_premise:
    # Check if the spending in the hypothesis contradicts the spending reported in the premise
    label = "contradiction"
elif hamburgers_hypothesis >= hamburgers_premise:
    # Check if the number of hamburgers in the hypothesis contradicts the number of hamburgers reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
