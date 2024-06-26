# define the variable for the share of Deepak
deepak_share_premise = 1300
deepak_share_hypothesis = 1300

# the hypothesis gives an estimate for Deepak's share
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
