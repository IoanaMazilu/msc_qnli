outfits_premise = 7200
outfits_hypothesis = 6200

# the hypothesis refers to the number of different outfits Dave can make, mentioned in the premise
if outfits_hypothesis != outfits_premise:
    # check if the number of different outfits in the hypothesis contradicts the number of different outfits reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
