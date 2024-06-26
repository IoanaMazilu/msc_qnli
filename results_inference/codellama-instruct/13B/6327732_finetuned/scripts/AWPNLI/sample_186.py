num_boats_premise = 5.0
num_people_per_boat_premise = 3.0
num_people_hypothesis = 15.0

# the hypothesis refers to the number of people on boats, which are also mentioned in the premise
# compute the total number of people in the premise
total_people_premise = num_boats_premise * num_people_per_boat_premise
if num_people_hypothesis!= total_people_premise:
    # check if the number of people in the hypothesis contradicts the number of people from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
