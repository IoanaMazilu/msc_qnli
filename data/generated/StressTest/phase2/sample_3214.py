# Premise: In Kaya's teacher's desk there are less than 60 pink highlighters, 15 yellow highlighters, and 8 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are 10 pink highlighters, 15 yellow highlighters, and 8 blue highlighters.
# Golden Label: neutral

pink_highlighters_premise = 60
pink_highlighters_hypothesis = 10
yellow_highlighters_premise = 15
yellow_highlighters_hypothesis = 15
blue_highlighters_premise = 8
blue_highlighters_hypothesis = 8

# the hypothesis refers to the number of pink, yellow and blue highlighters in Kaya's teacher's desk, which is also mentioned in the premise
if pink_highlighters_hypothesis >= pink_highlighters_premise:
    # check if the number of pink highlighters in the hypothesis contradicts the estimate of less than 'pink_highlighters_premise' in the premise
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters in the premise
    label = "contradiction"
elif blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters in the premise
    label = "contradiction"
else:
    # if the hypothesis' numbers do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

