carton_length_premise = 25
carton_width_premise = 42
carton_height_premise = 60
carton_length_hypothesis = 25
carton_width_hypothesis = 42
carton_height_hypothesis = 60

# the hypothesis refers to the dimensions of the cartons mentioned in the premise
if carton_length_hypothesis <= carton_length_premise or carton_width_hypothesis <= carton_width_premise or carton_height_hypothesis <= carton_height_premise:
    # check if the hypothesis dimensions contradict the premise dimensions
    label = "contradiction"
else:
    # the premise gives exact measurements for the cartons
    # any dimensions greater than the premise ones cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
