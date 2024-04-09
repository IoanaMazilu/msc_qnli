people_premise = 8
people_hypothesis = 6

# the hypothesis refers to the number of people that can be seated on a bench, mentioned also in the premise
if people_hypothesis >= people_premise:
    # check if the number of people in the hypothesis contradicts the premise of less than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
