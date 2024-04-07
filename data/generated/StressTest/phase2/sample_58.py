# Premise: If Dave has more than one of each of the listed garments, and can make more than 1400 different outfits, then for how many garments does Dave have exactly five choices?
# Hypothesis: If Dave has more than one of each of the listed garments, and can make 2400 different outfits, then for how many garments does Dave have exactly five choices?
# Golden Label: neutral

outfits_premise = 1400
outfits_hypothesis = 2400

# both premise and hypothesis talk about the number of different outfits Dave can make
if outfits_premise >= outfits_hypothesis:
    # check if the number of outfits in the hypothesis contradicts the estimate of more than 'outfits_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of outfits
    # any number of outfits greater than 'outfits_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

