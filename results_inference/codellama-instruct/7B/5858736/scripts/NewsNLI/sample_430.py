building_premise = 1
building_hypothesis = 1

# the hypothesis mentions that at least one building has been damaged, which is also mentioned in the premise
if building_hypothesis!= building_premise:
    # check if the number of damaged buildings in the hypothesis contradicts the number of damaged buildings in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
