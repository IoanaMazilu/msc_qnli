econ_class_premise = 64
econ_class_hypothesis = 24
marketing_class_premise = 28
marketing_class_hypothesis = 28
stats_class_premise = 18
stats_class_hypothesis = 18

# the hypothesis refers to the number of names on the rosters for the economics, marketing and statistics classes mentioned in the premise
if econ_class_hypothesis >= econ_class_premise:
    # check if the number of names in the economics class roster in the hypothesis contradicts the premise
    label = "contradiction"
elif marketing_class_hypothesis != marketing_class_premise or stats_class_hypothesis != stats_class_premise:
    # check if the number of names in the marketing or statistics class rosters in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
