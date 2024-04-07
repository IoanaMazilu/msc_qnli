# Premise: In Kaya's teacher's desk there are 3 pink highlighters, 7 yellow highlighters, and 5 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are less than 4 pink highlighters, 7 yellow highlighters, and 5 blue highlighters.
# Golden Label: entailment

pink_highlighters_premise = 3
pink_highlighters_hypothesis = 4
yellow_highlighters_premise = 7
yellow_highlighters_hypothesis = 7
blue_highlighters_premise = 5
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of each color of highlighters mentioned in the premise
if pink_highlighters_hypothesis <= pink_highlighters_premise:
    # check if the estimate of 'pink_highlighters_hypothesis' contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise or blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of yellow or blue highlighters in the hypothesis contradicts the number of yellow or blue highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

