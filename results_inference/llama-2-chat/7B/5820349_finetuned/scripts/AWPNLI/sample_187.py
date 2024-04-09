boats_premise = 5.0
people_per_boat_premise = 3.0
people_on_boats_hypothesis = 19.0

# the hypothesis refers to the number of people on boats, which is also calculated in the premise
# compute the total number of people on boats in the premise
people_on_boats_premise = boats_premise * people_per_boat_premise
if people_on_boats_hypothesis!= people_on_boats_premise:
    # check if the number of people on boats in the hypothesis contradicts the number of people on boats from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
