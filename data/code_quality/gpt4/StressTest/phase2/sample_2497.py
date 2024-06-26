people_surveyed_premise = 810
people_surveyed_hypothesis = 110

# the hypothesis talks about the number of people surveyed in a town, mentioned also in the premise
if people_surveyed_hypothesis >= people_surveyed_premise:
    # check if the hypothesis value contradicts the estimation of less than 'people_surveyed_premise'
    label = "contradiction"
elif people_surveyed_hypothesis < people_surveyed_premise:
    # the premise gives only an estimate for the number of people surveyed
    # any number of people surveyed less than 'people_surveyed_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
