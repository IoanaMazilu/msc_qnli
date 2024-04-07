# Premise: In Kaya's teacher's desk there are 10 pink highlighters, 15 yellow highlighters, and 8 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are more than 10 pink highlighters, 15 yellow highlighters, and 8 blue highlighters.
# Golden Label: contradiction

pink_highlighters_premise = 10
pink_highlighters_hypothesis = 10
yellow_highlighters_premise = 15
yellow_highlighters_hypothesis = 15
blue_highlighters_premise = 8
blue_highlighters_hypothesis = 8

# the hypothesis refers to the number of each type of highlighters in the teacher's desk mentioned in the premise
if pink_highlighters_hypothesis > pink_highlighters_premise:
    # check if the hypothesis estimate of more than 'pink_highlighters_hypothesis' contradicts the actual number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise or blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of yellow highlighters or blue highlighters in the hypothesis contradicts the actual number of the respective highlighters in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

