chocolates_premise = 15
chocolates_hypothesis = 55
children_premise = 5
children_hypothesis = 5

# the hypothesis refers to the number of chocolates Zada has to distribute among her children, just like the premise
if chocolates_hypothesis <= chocolates_premise:
    # check if the estimate of 'chocolates_hypothesis' contradicts the number of chocolates in the premise
    label = "contradiction"
elif children_hypothesis != children_premise:
    # check if the number of children in the hypothesis contradicts the number of children reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
