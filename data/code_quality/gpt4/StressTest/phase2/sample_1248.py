outfits_premise = 7200
outfits_hypothesis = 3200

# the hypothesis refers to the number of outfits Dave can make, mentioned in the premise
if outfits_premise < outfits_hypothesis:
    # check if the estimate of 'outfits_hypothesis' contradicts the number of outfits in the premise
    label = "contradiction"
else:
    # the premise gives an exact number for the outfits
    # any number of outfits less than 'outfits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
