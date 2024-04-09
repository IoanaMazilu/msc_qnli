people_premise = 5
people_hypothesis = 6

# the hypothesis refers to the number of people that can be seated on the bench,
# while the premise gives the specific constraint on Rohit's seating
if people_hypothesis <= people_premise:
    # check if the estimate of 'people_hypothesis' contradicts the premise
    label = "contradiction"
elif people_premise!= people_hypothesis:
    # check if the number of people that can be seated in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
