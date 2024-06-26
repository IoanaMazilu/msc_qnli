number_people_premise = 85
number_people_hypothesis = 85

# the hypothesis and premise mention the number of richest people in the world
if number_people_premise!= number_people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
