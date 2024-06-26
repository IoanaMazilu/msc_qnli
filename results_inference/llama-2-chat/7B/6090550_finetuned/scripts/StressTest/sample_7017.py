ys_premise = 300
ys_hypothesis = 800
pc_premise = 0.4
pc_hypothesis = 0.4

# the hypothesis refers to the number of seniors and the percentage of seniors with cars, both mentioned in the premise
if ys_hypothesis <= ys_premise:
    # check if the estimate of 'ys_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
elif pc_hypothesis!= pc_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
