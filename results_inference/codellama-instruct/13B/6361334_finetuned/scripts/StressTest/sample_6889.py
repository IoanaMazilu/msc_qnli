num_people_premise = 8
num_people_hypothesis = 6

# the hypothesis refers to the number of people that can be seated on a bench, which is also mentioned in the premise
if num_people_hypothesis > num_people_premise:
    # check if the hypothesis value contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives an estimate for the number of people that cannot be seated on a bench
    # any number of people less than or equal to 'num_people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
