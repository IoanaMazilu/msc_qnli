boats_premise = 3.0
people_boats_premise = 5.0
people_per_boat_hypothesis = 5.5

# the hypothesis refers to the number of people per boat, which is also mentioned in the premise
# compute the average number of people per boat from the premise
average_people_per_boat = people_boats_premise / boats_premise
if average_people_per_boat!= people_per_boat_hypothesis:
    # check if the average number of people per boat in the hypothesis contradicts the average number of people per boat from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
