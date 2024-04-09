left_position_premise = 4
right_position_premise = 62
left_position_hypothesis = 12

# the hypothesis talks about the position of Rahul in the line, referenced also in the premise
if left_position_hypothesis <= left_position_premise:
    # check if the hypothesis value contradicts the estimate of 'left_position_premise'
    label = "contradiction"
elif right_position_premise - left_position_premise!= right_position_hypothesis - left_position_hypothesis:
    # check if the estimate of the number of boys to be added in the hypothesis contradicts the estimate of the number of boys to be added in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the position of Rahul in the line
    # any position of Rahul greater than 'left_position_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
