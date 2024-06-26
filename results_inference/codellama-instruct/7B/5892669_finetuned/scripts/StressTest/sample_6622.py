committee_size_premise = 5
committee_size_hypothesis = 4
people_premise = 7
people_hypothesis = 7

# the hypothesis refers to the number of people and committee size mentioned in the premise
if committee_size_hypothesis >= committee_size_premise:
    # check if the committee size in the hypothesis contradicts the estimate of less than 'committee_size_premise'
    label = "contradiction"
elif people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the committee size
    # any committee size less than 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
