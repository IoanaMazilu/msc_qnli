sensex_down_premise = 362.75
sensex_down_hypothesis = 357.39

# the hypothesis and premise mention the amount by which Sensex has gone down
if sensex_down_hypothesis != sensex_down_premise:
    # check if the amount by which Sensex has gone down in the hypothesis contradicts the amount in the premise
    label = "contradiction"
else:
    # if the Sensex values in the hypothesis do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
