shares_sam_premise = 5000
shares_sam_hypothesis = 2000

# the hypothesis refers to the number of shares Sam owns, mentioned also in the premise
if shares_sam_hypothesis >= shares_sam_premise:
    # check if the number of shares in the hypothesis contradicts the premise statement of Sam owning less than 'shares_sam_premise'
    label = "contradiction"
elif shares_sam_hypothesis < shares_sam_premise:
    # the premise gives only an estimate for the number of shares Sam owns
    # any number of shares less than 'shares_sam_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
