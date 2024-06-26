ashok_share_premise = 4/9
ashok_share_hypothesis = 1/9

# the hypothesis talks about the share of Ashok in the capital, also mentioned in the premise
if ashok_share_hypothesis > ashok_share_premise:
    # check if the hypothesis value contradicts the premise of less than 'ashok_share_premise'
    label = "contradiction"
elif ashok_share_hypothesis != ashok_share_premise:
    # the premise gives only a limit for the share of Ashok
    # any share less than 'ashok_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the share of Ashok in the hypothesis is exactly equal to 'ashok_share_premise', we can infer entailment
    label = "entailment"

print(label)
