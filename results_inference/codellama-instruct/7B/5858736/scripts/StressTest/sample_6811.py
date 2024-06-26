seniors_premise = 500
seniors_hypothesis = 300
cars_premise = 0.5
cars_hypothesis = 0.5

if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the estimate of less than'seniors_premise'
    label = "contradiction"
elif cars_hypothesis!= cars_premise:
    # check if the percentage of cars in the hypothesis contradicts the percentage of cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
