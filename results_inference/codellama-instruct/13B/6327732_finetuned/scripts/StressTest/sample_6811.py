seniors_premise = 500
seniors_hypothesis = 300
cars_premise = 50
cars_hypothesis = 50

# the hypothesis refers to the number of seniors and the percentage of them with cars, both mentioned in the premise
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of less than'seniors_premise'
    label = "contradiction"
elif cars_hypothesis!= cars_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
