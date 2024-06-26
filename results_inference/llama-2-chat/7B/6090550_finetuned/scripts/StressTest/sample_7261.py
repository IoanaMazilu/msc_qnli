carol_rectangle_length_premise = 52
carol_rectangle_length_hypothesis = 12
jordan_rectangle_length_premise = 9
jordan_rectangle_length_hypothesis = 9

# the hypothesis talks about the measurements of Carol's and Jordan's rectangles, referenced also in the premise
if carol_rectangle_length_hypothesis <= carol_rectangle_length_premise:
    # check if the hypothesis value for Carol's rectangle length contradicts the premise
    label = "contradiction"
elif jordan_rectangle_length_hypothesis!= jordan_rectangle_length_premise:
    # check if the hypothesis value for Jordan's rectangle length contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
