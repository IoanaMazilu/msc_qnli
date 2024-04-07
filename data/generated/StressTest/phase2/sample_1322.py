# Premise: Zimmer has 237 papers to hand out to his class.
# Hypothesis: Zimmer has 137 papers to hand out to his class.
# Golden Label: contradiction

papers_premise = 237
papers_hypothesis = 137

# the hypothesis refers to the number of papers that Zimmer has to hand out, as mentioned in the premise
if papers_hypothesis != papers_premise:
    # check if the number of papers in the hypothesis contradicts the number of papers reported in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

