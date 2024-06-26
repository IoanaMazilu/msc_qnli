# define variables for the dimensions of Carol's and Jordan's rectangles
carol_rectangle_width_premise = 52
carol_rectangle_width_hypothesis = 12
jordan_rectangle_width_premise = 9
jordan_rectangle_width_hypothesis = 9

# the hypothesis talks about the dimensions of Carol's and Jordan's rectangles, referenced also in the premise
if carol_rectangle_width_hypothesis >= carol_rectangle_width_premise:
    # check if the hypothesis value contradicts the estimate of less than 'carol_rectangle_width_premise'
    label = "contradiction"
elif jordan_rectangle_width_hypothesis!= jordan_rectangle_width_premise:
    # check if the number of Jordan's rectangle width in the hypothesis contradicts the number of Jordan's rectangle width reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
