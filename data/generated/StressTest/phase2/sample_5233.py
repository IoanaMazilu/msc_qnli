# Premise: less than 3000, Deepak's share is :
# Hypothesis: 2000, Deepak's share is :
# Golden Label: neutral

deepak_share_premise = 3000
deepak_share_hypothesis = 2000

# the hypothesis talks about Deepak's share, which is also mentioned in the premise
if deepak_share_hypothesis >= deepak_share_premise:
    # check if the hypothesis value contradicts the estimate of less than 'deepak_share_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for Deepak's share
    # any share less than 'deepak_share_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

