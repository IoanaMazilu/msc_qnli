# Premise: 4.0 birds were sitting on the fence and 2.0 more birds flew away.
# Hypothesis: 3.0 birds are now sitting on the fence.
# Golden Label: contradiction

sitting_birds_premise = 4.0
flew_away_birds_premise = 2.0
sitting_birds_hypothesis = 3.0

# the hypothesis refers to the number of birds sitting on the fence, which is also referenced in the premise
# compute the number of birds sitting on the fence after the birds flew away
sitting_birds_after_flyaway_premise = sitting_birds_premise - flew_away_birds_premise
if sitting_birds_hypothesis != sitting_birds_after_flyaway_premise:
    # check if the number of birds in the hypothesis contradicts the number of birds from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

