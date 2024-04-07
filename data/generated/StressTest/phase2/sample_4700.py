# Premise: In Kaya's teacher's desk there are 6 pink highlighters, 2 yellow highlighters, and 4 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are less than 6 pink highlighters, 2 yellow highlighters, and 4 blue highlighters.
# Golden Label: contradiction

pink_highlighters_premise = 6
pink_highlighters_hypothesis = 6
yellow_highlighters_premise = 2
yellow_highlighters_hypothesis = 2
blue_highlighters_premise = 4
blue_highlighters_hypothesis = 4

# The hypothesis refers to the number of each type of highlighter in the teacher's desk mentioned in the premise
if pink_highlighters_hypothesis >= pink_highlighters_premise:
    # Check if the estimate of 'pink_highlighters_hypothesis' contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise:
    # Check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters reported in the premise
    label = "contradiction"
elif blue_highlighters_hypothesis != blue_highlighters_premise:
    # Check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

