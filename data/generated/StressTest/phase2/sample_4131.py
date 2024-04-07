# Premise: If Carol's rectangle measures 15 inches by 24 inches and Jordan's rectangle is 8 inches long, how wide is Jordan's rectangle, in inches?
# Hypothesis: If Carol's rectangle measures less than 55 inches by 24 inches and Jordan's rectangle is 8 inches long, how wide is Jordan's rectangle, in inches?
# Golden Label: entailment

carol_rectangle_length_premise = 15
carol_rectangle_width_premise = 24
jordan_rectangle_length_premise = 8

carol_rectangle_length_hypothesis = 55
carol_rectangle_width_hypothesis = 24
jordan_rectangle_length_hypothesis = 8

# the hypothesis talks about the measurements of the rectangles mentioned also in the premise
if carol_rectangle_length_hypothesis <= carol_rectangle_length_premise:
    # check if the estimate of 'carol_rectangle_length_hypothesis' contradicts the measurement reported in the premise
    label = "contradiction"
elif carol_rectangle_width_hypothesis != carol_rectangle_width_premise:
    # check if the measurement of Carol's rectangle's width in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
elif jordan_rectangle_length_hypothesis != jordan_rectangle_length_premise:
    # check if the measurement of Jordan's rectangle's length in the hypothesis contradicts the one reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

