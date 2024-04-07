# Premise: If Dave has more than one of each of the listed garments, and can make 7200 different outfits, then for how many garments does Dave have exactly five choices?
# Hypothesis: If Dave has more than one of each of the listed garments, and can make more than 3200 different outfits, then for how many garments does Dave have exactly five choices?
# Golden Label: entailment

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

