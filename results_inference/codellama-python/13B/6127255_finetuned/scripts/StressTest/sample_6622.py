committee_size_premise = 5
committee_size_hypothesis = 4
people_premise = 7
people_hypothesis = 7

# the hypothesis refers to the size of the committee and the number of people, both mentioned in the premise
if committee_size_hypothesis >= committee_size_premise:
    # check if the size of the committee in the hypothesis contradicts the premise's condition of less than 'committee_size_premise'
    label = "contradiction"
elif people_hypothesis!= people_premise:
    # check if the number of people in the hypothesis contradicts the number of people in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the size of the committee
    # any size less than 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
# 