boats_premise = 3.0
people_premise = 5.0
average_people_hypothesis = 5.5

# the hypothesis refers to the average number of people in each boat, which can be calculated from the premise
# compute the average number of people in each boat in the premise
average_people_premise = people_premise / boats_premise
if average_people_hypothesis!= average_people_premise:
    # check if the average number of people in each boat in the hypothesis contradicts the average number of people in each boat in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
