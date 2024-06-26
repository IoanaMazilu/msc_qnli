deepak_share_premise = 1300
deepak_share_hypothesis = 1300

# the hypothesis refers to the Deepak's share mentioned in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise, it can be entailed from the premise
    label = "entailment"

print(label)
