people_premise = 1
people_hypothesis = 8

# the hypothesis talks about the number of people from which a committee is to be selected, referenced also in the premise
if people_hypothesis <= people_premise:
    # check if the number of people in the hypothesis contradicts the estimate of more than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people greater than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
