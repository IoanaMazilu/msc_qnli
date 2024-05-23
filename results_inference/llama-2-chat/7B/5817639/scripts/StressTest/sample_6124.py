people_premise = 20
people_hypothesis = 60

# the hypothesis refers to the number of people in the group, which is also mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the estimate of 'people_hypothesis' contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people, and any number greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)