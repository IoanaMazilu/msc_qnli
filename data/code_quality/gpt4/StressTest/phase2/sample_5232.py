deepak_share_premise = 2000
deepak_share_hypothesis = 3000

# the hypothesis talks about Deepak's share, referenced also in the premise
if deepak_share_premise >= deepak_share_hypothesis:
    # check if the premise value contradicts the estimate of less than 'deepak_share_hypothesis'
    label = "contradiction"
else:
    # the premise gives an exact number for Deepak's share
    # any number greater than 'deepak_share_premise' and less than 'deepak_share_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
