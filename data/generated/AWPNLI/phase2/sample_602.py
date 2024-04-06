# Premise: There are 3.0 boats on the lake and there are 5.0 people total in the boats.
# Hypothesis: 1.66666666667 people are in each boat on average.
# Golden Label: entailment

boats_premise = 3.0
people_premise = 5.0
average_people_per_boat_hypothesis = 1.66666666667

# the hypothesis refers to the average number of people per boat, which can be computed from the premise values
# compute the average number of people per boat in the premise
average_people_per_boat_premise = people_premise / boats_premise

if average_people_per_boat_hypothesis != average_people_per_boat_premise:
    # check if the average number of people per boat in the hypothesis contradicts the same value computed from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

