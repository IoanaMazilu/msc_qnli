seniors_premise = 300
seniors_hypothesis = 300
cars_seniors_premise = 0.5
cars_seniors_hypothesis = 0.5

# the hypothesis refers to the number of seniors and the percentage of seniors with cars mentioned in the premise
if seniors_hypothesis >= seniors_premise:
    # check if the estimate of'seniors_hypothesis' contradicts the number of seniors in the premise
    label = "contradiction"
elif cars_seniors_hypothesis!= cars_seniors_premise:
    # check if the percentage of seniors with cars in the hypothesis contradicts the percentage of seniors with cars reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)