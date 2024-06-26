boys_premise = 6
girls_premise = 4
committee_size_premise = 4
committee_size_hypothesis = 2

# the hypothesis refers to the number of committee members, which is also mentioned in the premise
if committee_size_hypothesis <= committee_size_premise:
    # check if the hypothesis value contradicts the number of committee members in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of committee members
    # any number of committee members greater than 'committee_size_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
