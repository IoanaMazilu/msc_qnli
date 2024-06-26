num_boats_premise = 3.0
num_people_premise = 5.0
avg_people_per_boat_hypothesis = 5.5

# the hypothesis refers to the number of people in each boat, which are also mentioned in the premise
# compute the total number of people in the premise
total_people_premise = num_boats_premise * num_people_premise
if avg_people_per_boat_hypothesis!= total_people_premise / num_boats_premise:
    # check if the average number of people per boat in the hypothesis contradicts the average number of people per boat from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
