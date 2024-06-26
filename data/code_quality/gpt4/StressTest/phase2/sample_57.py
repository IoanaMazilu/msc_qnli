outfits_premise = 2400
outfits_hypothesis = 1400

# the hypothesis refers to the number of outfits Dave can make, which is also mentioned in the premise
if outfits_hypothesis >= outfits_premise:
    # check if the estimate of 'outfits_hypothesis' contradicts the number of outfits in the premise
    label = "contradiction"
else:
    # if the hypothesis estimate does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
