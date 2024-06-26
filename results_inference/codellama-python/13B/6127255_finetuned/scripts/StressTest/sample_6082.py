position_right_premise = 62
position_right_hypothesis = 12
position_left = 4
boys_in_line_premise = 28
boys_in_line_hypothesis = 28

# the hypothesis refers to the position of Rahul and the number of boys in the line, both mentioned in the premise
if position_right_hypothesis >= position_right_premise:
    # check if the hypothesis value contradicts the estimate of less than 'position_right_premise'
    label = "contradiction"
elif boys_in_line_hypothesis!= boys_in_line_premise:
    # check if the number of boys in the line in the hypothesis contradicts the number of boys in the line reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the position of Rahul
    # any position less than 'position_right_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
