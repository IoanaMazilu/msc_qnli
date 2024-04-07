# Premise: In Kaya's teacher's desk there are 10 pink highlighters, 15 yellow highlighters, and 8 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are less than 60 pink highlighters, 15 yellow highlighters, and 8 blue highlighters.
# Golden Label: entailment

pink_highlighters_premise = 10
pink_highlighters_hypothesis = 60
yellow_highlighters_premise = 15
yellow_highlighters_hypothesis = 15
blue_highlighters_premise = 8
blue_highlighters_hypothesis = 8

# hypothesis refers to the number of pink, yellow and blue highlighters mentioned in the premise.
if pink_highlighters_premise > pink_highlighters_hypothesis:
    # check if the estimate of 'pink_highlighters_hypothesis' contradicts the number of pink highlighters in the premise
    label = "contradiction"
elif yellow_highlighters_premise != yellow_highlighters_hypothesis:
    # check if the number of yellow highlighters in the hypothesis contradicts the number of yellow highlighters reported in the premise
    label = "contradiction"
elif blue_highlighters_premise != blue_highlighters_hypothesis:
    # check if the number of blue highlighters in the hypothesis contradicts the number of blue highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

