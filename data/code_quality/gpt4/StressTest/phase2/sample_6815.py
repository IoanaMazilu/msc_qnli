car_owners_premise = 18
car_owners_hypothesis = 58

# the hypothesis refers to the students at Morse having cars, also mentioned in the premise
if car_owners_hypothesis != car_owners_premise:
    # check if the proportion of car owners in the hypothesis contradicts the proportion in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
