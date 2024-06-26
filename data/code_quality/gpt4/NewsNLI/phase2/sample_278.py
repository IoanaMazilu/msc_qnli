suit_value_premise = 1000000000
suit_value_hypothesis = 1000000000

# the hypothesis mentions the value of the suit filed against the NBA which is also mentioned in the premise
if suit_value_hypothesis != suit_value_premise:
    # check if the suit value in the hypothesis contradicts the suit value reported in the premise
    label = "contradiction"
else:
    # if the hypothesis suit value does not contradict the premise suit value, we can infer entailment
    label = "entailment"

print(label)
