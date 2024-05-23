people_seating_premise = 2
people_seating_hypothesis = 5

# the hypothesis refers to the number of people that can be seated on a bench, mentioned in the premise
if people_seating_hypothesis <= people_seating_premise:
    # check if the number of people in the hypothesis contradicts the estimate of more than 'people_seating_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_seating_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)