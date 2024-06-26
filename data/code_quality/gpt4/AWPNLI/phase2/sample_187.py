boats_premise = 5.0
people_per_boat_premise = 3.0
people_hypothesis = 19.0

# the hypothesis refers to the total number of people on boats, which can be computed from the premise
# compute the total number of people on boats in the premise
total_people_premise = boats_premise * people_per_boat_premise
if total_people_premise != people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
