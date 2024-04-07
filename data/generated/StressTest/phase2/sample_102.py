# Premise: In Kaya's teacher's desk there are 4 pink highlighters, 2 yellow highlighters, and 5 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are more than 3 pink highlighters, 2 yellow highlighters, and 5 blue highlighters.
# Golden Label: entailment

pink_highlighters_premise = 4
pink_highlighters_hypothesis = 3
yellow_highlighters_premise = 2
yellow_highlighters_hypothesis = 2
blue_highlighters_premise = 5
blue_highlighters_hypothesis = 5

# the hypothesis refers to the number of highlighters of each color in Kaya's teacher's desk, mentioned also in the premise
if pink_highlighters_premise <= pink_highlighters_hypothesis:
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

