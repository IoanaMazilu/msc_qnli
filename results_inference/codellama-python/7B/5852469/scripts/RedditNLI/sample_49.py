number_people_premise = 7.5
number_people_hypothesis = 7.5

# the hypothesis and premise mention the same number of people
if number_people_premise!= number_people_hypothesis:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise and hypothesis mention the same number of people
    # any estimate of the number of people in the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
