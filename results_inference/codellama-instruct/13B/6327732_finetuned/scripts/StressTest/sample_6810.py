seniors_premise = 300
seniors_hypothesis = 500
cars_premise = 0.5
cars_hypothesis = 0.5

# the hypothesis refers to the number of seniors and the percentage of them with cars
# the premise mentions the number of seniors and the percentage of them with cars
if seniors_hypothesis <= seniors_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif cars_hypothesis!= cars_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)