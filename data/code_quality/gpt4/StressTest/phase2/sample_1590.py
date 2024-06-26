share_sravan_premise = 5535
share_sravan_hypothesis = 7535

# the hypothesis refers to Sravan's share mentioned in the premise
if share_sravan_hypothesis <= share_sravan_premise:
    # check if the hypothesis value contradicts the exact value of 'share_sravan_premise'
    label = "contradiction"
else:
    # the hypothesis provides an upper limit for Sravan's share, which is consistent with the premise but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
