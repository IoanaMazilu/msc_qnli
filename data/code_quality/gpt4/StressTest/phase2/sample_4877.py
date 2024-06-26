people_pool_premise = 8
people_pool_hypothesis = 3

# the hypothesis refers to the number of people from which a committee is to be selected
if people_pool_hypothesis != people_pool_premise:
    # check if the number of people in the hypothesis contradicts the number of people mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
