gangs_premise = 3
gangs_hypothesis = 7

# the hypothesis refers to the number of gangs in a friendship gang, which is also mentioned in the premise
if gangs_hypothesis!= gangs_premise:
    # check if the number of gangs in the hypothesis contradicts the number of gangs in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
