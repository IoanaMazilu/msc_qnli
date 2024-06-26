people_moon_premise = 12
people_moon_hypothesis = 13

# the hypothesis talks about the number of people who have been to the moon
if people_moon_hypothesis <= people_moon_premise:
    # check if the hypothesis value contradicts the estimate of 'people_moon_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of people who have been to the moon
    # any number of people greater than 'people_moon_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
