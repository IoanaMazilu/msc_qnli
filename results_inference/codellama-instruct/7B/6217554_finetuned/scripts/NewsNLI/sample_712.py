souvenirs_value_premise = 100000
souvenirs_value_hypothesis = 100000

# the hypothesis mentions the value of the souvenirs, which is also referenced in the premise
if souvenirs_value_hypothesis!= souvenirs_value_premise:
    # check if the value of the souvenirs from the hypothesis contradicts the value of the souvenirs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
