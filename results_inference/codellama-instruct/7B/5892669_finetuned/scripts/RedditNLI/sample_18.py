sensex_close_premise = 362.75
sensex_close_hypothesis = 357.39

# the hypothesis and premise mention the closing value of Sensex
if sensex_close_hypothesis!= sensex_close_premise:
    # check if the closing value of Sensex in the hypothesis contradicts the closing value in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
