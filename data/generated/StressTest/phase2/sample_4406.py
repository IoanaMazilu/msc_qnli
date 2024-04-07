# Premise: In Kaya's teacher's desk there are 3 pink highlighters, 7 yellow highlighters, and 5 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are 1 pink highlighters, 7 yellow highlighters, and 5 blue highlighters.
# Golden Label: contradiction

pink_highlighters_premise = 3
yellow_highlighters_premise = 7
blue_highlighters_premise = 5

pink_highlighters_hypothesis = 1
yellow_highlighters_hypothesis = 7
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of each color highlighters mentioned in the premise
if pink_highlighters_hypothesis != pink_highlighters_premise:
    # check if the number of pink highlighters in the hypothesis contradicts the number of pink highlighters reported in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters reported in the premise
    label = "contradiction"
elif blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

