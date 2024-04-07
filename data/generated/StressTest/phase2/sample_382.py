# Premise: If Carol's rectangle measures less than 62 inches by 15 inches and Jordan's rectangle is 6 inches long, how wide is Jordan's rectangle, in inches?
# Hypothesis: If Carol's rectangle measures 12 inches by 15 inches and Jordan's rectangle is 6 inches long, how wide is Jordan's rectangle, in inches?
# Golden Label: neutral

carol_rectangle_length_premise = 62
carol_rectangle_length_hypothesis = 12
carol_rectangle_width_premise = 15
carol_rectangle_width_hypothesis = 15
jordan_rectangle_length_premise = 6
jordan_rectangle_length_hypothesis = 6

# the hypothesis refers to the size of Carol's and Jordan's rectangles mentioned in the premise
if carol_rectangle_length_hypothesis >= carol_rectangle_length_premise:
    # check if the size of 'carol_rectangle_length_hypothesis' contradicts the size of Carol's rectangle in the premise
    label = "contradiction"
elif carol_rectangle_width_hypothesis != carol_rectangle_width_premise or jordan_rectangle_length_hypothesis != jordan_rectangle_length_premise:
    # check if the size of Carol's rectangle width or Jordan's rectangle length in the hypothesis contradicts the size reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

