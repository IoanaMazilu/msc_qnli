# Premise: 4.0 birds were sitting on the fence and 2.0 more birds flew away.
# Hypothesis: 2.0 birds are now sitting on the fence.
# Golden Label: entailment

sitting_birds_premise = 4.0
flew_away_birds_premise = 2.0
sitting_birds_hypothesis = 2.0

# the hypothesis refers to the number of birds sitting on the fence, which is also mentioned in the premise
# compute the number of birds sitting on the fence after some birds flew away
sitting_birds_after_premise = sitting_birds_premise - flew_away_birds_premise
if sitting_birds_hypothesis != sitting_birds_after_premise:
    # check if the number of birds sitting in the hypothesis contradicts the number of birds sitting after some flew away in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)

