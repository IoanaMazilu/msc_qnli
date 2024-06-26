outfits_premise = 2400
outfits_hypothesis = 2400

# the hypothesis refers to the amount of outfits Dave can make, which is also mentioned in the premise
if outfits_hypothesis > outfits_premise:
    # check if the estimate of 'outfits_hypothesis' contradicts the number of outfits in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
