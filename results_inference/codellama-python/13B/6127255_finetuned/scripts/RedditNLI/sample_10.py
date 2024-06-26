rupee_premise = 65.36
rupee_hypothesis = 68.19
sensex_premise = 300
sensex_hypothesis = 282.50

# the hypothesis and premise mention the value of the rupee and the Sensex
if rupee_hypothesis > rupee_premise:
    # check if the value of the rupee in the hypothesis contradicts the value of the rupee in the premise
    label = "contradiction"
elif sensex_hypothesis > sensex_premise:
    # check if the value of the Sensex in the hypothesis contradicts the value of the Sensex in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
