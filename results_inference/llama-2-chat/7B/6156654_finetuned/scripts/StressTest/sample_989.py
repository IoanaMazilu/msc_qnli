seniors_premise = 300
seniors_hypothesis = 300
cars_premise = 50
cars_hypothesis = 50

# the hypothesis refers to the number of seniors and cars, which are also mentioned in the premise
if seniors_hypothesis!= seniors_premise:
    # check if the number of seniors in the hypothesis contradicts the number of seniors in the premise
    label = "contradiction"
elif cars_hypothesis!= cars_premise:
    # check if the number of cars in the hypothesis contradicts the number of cars in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
