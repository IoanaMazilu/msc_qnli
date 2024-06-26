people_premise = 42
people_hypothesis = 12

# the hypothesis is about the number of people in a BCCI meeting, which is also mentioned in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the estimate of less than 'people_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people
    # any number of people less than 'people_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
