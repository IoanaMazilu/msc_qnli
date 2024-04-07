# Premise: If Dave has more than one of each of the listed garments, and can make 2400 different outfits, then for how many garments does Dave have exactly five choices?
# Hypothesis: If Dave has more than one of each of the listed garments, and can make more than 2400 different outfits, then for how many garments does Dave have exactly five choices?
# Golden Label: contradiction

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

