people_seat_premise = 5
people_seat_hypothesis = 5

# the hypothesis refers to the number of people that can be seated on the bench, referenced also in the premise
if people_seat_hypothesis <= people_seat_premise:
    # check if the hypothesis value contradicts the number of people that can be seated on the bench in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people that can be seated on the bench
    # any number of people greater than 'people_seat_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
