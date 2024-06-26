girls = 2
boys = 2

# the hypothesis refers to the number of girls and boys, which are also mentioned in the premise
if girls >= 2 and boys == 2:
    # check if the number of girls in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
