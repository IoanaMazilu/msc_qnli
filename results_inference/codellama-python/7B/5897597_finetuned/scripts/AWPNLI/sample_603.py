boats_premise = 3.0
people_premise = 5.0
people_per_boat_hypothesis = 5.5

# the hypothesis refers to the average number of people per boat, which can be computed from the premise
# compute the average number of people per boat in the premise
people_per_boat_premise = people_premise / boats_premise
if people_per_boat_hypothesis!= people_per_boat_premise:
    # check if the average number of people per boat in the hypothesis contradicts the average number of people per boat from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
