deepak_share_premise = 4000
deepak_share_hypothesis = 2000

# the hypothesis talks about the amount of Deepak's share, mentioned also in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the hypothesis value contradicts the estimate of less than 'deepak_share_premise'
    label = "contradiction"
elif deepak_share_hypothesis < deepak_share_premise:
    # the premise gives only an estimate for the amount of Deepak's share
    # any amount of Deepak's share less than 'deepak_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
