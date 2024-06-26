tshirts_bought_premise = 8
tshirts_bought_hypothesis = 4

# the hypothesis refers to the number of t-shirts bought, which is also mentioned in the premise
if tshirts_bought_premise <= tshirts_bought_hypothesis:
    # check if the number of t-shirts in the hypothesis contradicts the number of t-shirts bought in the premise
    label = "contradiction"
else:
    # the hypothesis values and estimates do not contradict the premise ones, so we can infer entailment
    label = "entailment"

print(label)
