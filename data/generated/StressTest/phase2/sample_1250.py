# Premise: If Dave has more than one of each of the listed garments, and can make 7200 different outfits, then for how many garments does Dave have exactly five choices?
# Hypothesis: If Dave has more than one of each of the listed garments, and can make 6200 different outfits, then for how many garments does Dave have exactly five choices?
# Golden Label: contradiction

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

