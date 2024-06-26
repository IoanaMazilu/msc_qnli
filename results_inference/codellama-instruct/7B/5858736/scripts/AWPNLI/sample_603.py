boats_premise = 3.0
people_boats_premise = 5.0
people_boat_hypothesis = 5.5

# the hypothesis refers to the number of people in each boat, which are also mentioned in the premise
# compute the average number of people in each boat from the premise
average_people_boat_premise = people_boats_premise / boats_premise
if average_people_boat_hypothesis!= average_people_boat_premise:
    # check if the average number of people in each boat from the hypothesis contradicts the estimate from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
