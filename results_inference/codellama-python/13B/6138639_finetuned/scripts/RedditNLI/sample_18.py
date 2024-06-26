sensex_premise = 362.75
sensex_hypothesis = 357.39

# the hypothesis and premise mention the value of the Sensex
if sensex_hypothesis > sensex_premise:
    # check if the value of the Sensex in the hypothesis contradicts the value of the Sensex in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
