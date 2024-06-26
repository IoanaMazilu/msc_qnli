seniors_premise = 300
seniors_hypothesis = 400
cars_premise = 0.4
cars_hypothesis = 0.4

# the hypothesis refers to the number of seniors and the percentage of them with cars, both mentioned in the premise
if seniors_hypothesis!= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors reported in the premise
    label = "contradiction"
elif cars_hypothesis!= cars_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
