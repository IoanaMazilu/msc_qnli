num_people_premise = 6
num_people_hypothesis = 7

# the hypothesis refers to the number of people mentioned in the premise
if num_people_hypothesis <= num_people_premise:
    # check if the estimate of 'num_people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'num_people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
