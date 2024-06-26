sean_weight_premise = 200
sean_weight_hypothesis = 200
package1_weight = 150
package2_weight = 280

# the hypothesis talks about Sean's weight and the weight of two packages, all mentioned in the premise
if sean_weight_hypothesis < sean_weight_premise:
    # check if the hypothesis value contradicts the weight of Sean reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
