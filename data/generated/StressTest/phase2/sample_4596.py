# Premise: If Carol's rectangle measures 15 inches by 20 inches and Jordan's rectangle is 6 inches long, how wide is Jordan's rectangle, in inches?
# Hypothesis: If Carol's rectangle measures less than 65 inches by 20 inches and Jordan's rectangle is 6 inches long, how wide is Jordan's rectangle, in inches?
# Golden Label: entailment

carol_rectangle_length_premise = 15
carol_rectangle_width_premise = 20
jordan_rectangle_length_premise = 6

carol_rectangle_length_hypothesis = 65
carol_rectangle_width_hypothesis = 20
jordan_rectangle_length_hypothesis = 6

# the hypothesis refers to the measurements of Carol's and Jordan's rectangles mentioned in the premise
if carol_rectangle_length_hypothesis <= carol_rectangle_length_premise:
    # check if the estimate of 'carol_rectangle_length_hypothesis' contradicts the length of Carol's rectangle in the premise
    label = "contradiction"
elif carol_rectangle_width_hypothesis != carol_rectangle_width_premise:
    # check if the width of Carol's rectangle in the hypothesis contradicts the width of Carol's rectangle reported in the premise
    label = "contradiction"
elif jordan_rectangle_length_hypothesis != jordan_rectangle_length_premise:
    # check if the length of Jordan's rectangle in the hypothesis contradicts the length of Jordan's rectangle reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

