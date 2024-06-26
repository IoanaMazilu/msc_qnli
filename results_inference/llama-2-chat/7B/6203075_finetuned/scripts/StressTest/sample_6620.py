people_premise = 7
people_hypothesis = 7

# the hypothesis talks about the number of people from which a committee is to be selected, referenced also in the premise
if people_hypothesis >= people_premise:
    # check if the hypothesis value contradicts the premise of less than 'people_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than 'people_premise', it is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
