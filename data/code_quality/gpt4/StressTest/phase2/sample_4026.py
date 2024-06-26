people_premise = 6
people_hypothesis = 7

# the hypothesis refers to the number of people Richard will arrange, mentioned in the premise
if people_hypothesis <= people_premise:
    # check if the estimate of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
