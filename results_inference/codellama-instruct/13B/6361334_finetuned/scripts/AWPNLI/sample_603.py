num_boats_premise = 3.0
total_people_premise = 5.0
avg_people_per_boat_hypothesis = 5.5

# the hypothesis refers to the average number of people per boat, which is also mentioned in the premise
# compute the total number of people in the premise
total_people_premise = num_boats_premise * avg_people_per_boat_hypothesis
if total_people_premise!= total_people_premise:
    # check if the number of people in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
