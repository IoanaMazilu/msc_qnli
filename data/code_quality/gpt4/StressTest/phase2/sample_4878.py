committee_size_premise = 3
committee_size_hypothesis = 2
total_people = 8

# the hypothesis asks about the number of possible committees that can be formed from the total number of people mentioned in the premise
if committee_size_hypothesis >= committee_size_premise:
    # check if the estimate of 'committee_size_hypothesis' contradicts the number of people in the premise's committee
    label = "contradiction"
else:
    # The premise specifies a certain number of people in the committee
    # any number of people greater than 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
