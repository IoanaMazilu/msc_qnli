# Premise: In Kaya's teacher's desk there are less than 64 pink highlighters, 28 yellow highlighters, and 25 blue highlighters.
# Hypothesis: In Kaya's teacher's desk there are 24 pink highlighters, 28 yellow highlighters, and 25 blue highlighters.
# Golden Label: neutral

pink_highlighters_premise = 64
pink_highlighters_hypothesis = 24
yellow_highlighters_premise = 28
yellow_highlighters_hypothesis = 28
blue_highlighters_premise = 25
blue_highlighters_hypothesis = 25

# the hypothesis refers to the number of different colored highlighters in the teacher's desk, which is also mentioned in the premise
if pink_highlighters_hypothesis >= pink_highlighters_premise:
    # check if the hypothesis value contradicts the estimate of less than 'pink_highlighters_premise' 
    label = "contradiction"
elif yellow_highlighters_hypothesis != yellow_highlighters_premise or blue_highlighters_hypothesis != blue_highlighters_premise:
    # check if the number of yellow or blue highlighters in the hypothesis contradicts the number of yellow or blue highlighters reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

