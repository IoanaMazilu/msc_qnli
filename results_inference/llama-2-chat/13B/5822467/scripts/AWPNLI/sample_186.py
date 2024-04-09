boats_premise = 5.0
people_per_boat_premise = 3.0
total_people_hypothesis = 15.0

# compute the total number of boats in the hypothesis
total_boats_hypothesis = 15.0 / 3.0

# compare the total number of boats in the premise and the hypothesis
if total_boats_premise!= total_boats_hypothesis:
    # check if the number of boats in the hypothesis contradicts the number of boats from the premise
    label = "contradiction"
elif people_per_boat_premise * total_boats_premise!= total_people_hypothesis:
    # check if the total number of people in the hypothesis contradicts the product of the number of boats and people per boat from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
