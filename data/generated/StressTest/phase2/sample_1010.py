# Premise: If Carol's rectangle measures 8 inches by 15 inches and Jordan's rectangle is 4 inches long, how wide is Jordan's rectangle, in inches?
# Hypothesis: If Carol's rectangle measures 5 inches by 15 inches and Jordan's rectangle is 4 inches long, how wide is Jordan's rectangle, in inches?
# Golden Label: contradiction

carol_rectangle_length_premise = 8
carol_rectangle_length_hypothesis = 5
carol_rectangle_width = 15
jordan_rectangle_length = 4

# the hypothesis refers to the measurements of Carol's rectangle, and the length of Jordan's rectangle, all mentioned also in the premise
if carol_rectangle_length_hypothesis != carol_rectangle_length_premise:
    # check if the length of Carol's rectangle in the hypothesis contradicts the length mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and measurements do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

