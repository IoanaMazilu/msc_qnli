deepak_share_premise = 4300
deepak_share_hypothesis = 1300

# the hypothesis refers to the share of Deepak mentioned in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the value of 'deepak_share_hypothesis' contradicts the premise of less than 'deepak_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the share of Deepak
    # any share less than 'deepak_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
