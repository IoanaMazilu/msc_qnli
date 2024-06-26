outfits_premise = 3200
outfits_hypothesis = 7200

# the hypothesis talks about the number of different outfits Dave can make, mentioned also in the premise
if outfits_hypothesis <= outfits_premise:
    # check if the number of outfits in the hypothesis contradicts the estimate of more than 'outfits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of outfits
    # any number of outfits greater than 'outfits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
