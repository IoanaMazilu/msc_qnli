people_premise = 7
people_hypothesis = 7

# the hypothesis refers to the number of people from which a committee is to be selected, mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)