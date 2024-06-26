seniors_premise = 300
seniors_hypothesis = 600
cars_premise = 0.5
cars_hypothesis = 0.5

# the hypothesis refers to the number of seniors and the percentage of them with cars
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the number of seniors in the premise
    label = "contradiction"
elif cars_hypothesis!= cars_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
