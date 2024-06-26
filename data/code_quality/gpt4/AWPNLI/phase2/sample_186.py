boats_premise = 5.0
people_per_boat_premise = 3.0
total_people_hypothesis = 15.0

# the hypothesis refers to the total number of people on boats, which is dependent on the number of boats and people per boat in the premise
# compute the total number of people in the premise
total_people_premise = boats_premise * people_per_boat_premise

if total_people_hypothesis != total_people_premise:
    # check if the total number of people in the hypothesis contradicts the total number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
