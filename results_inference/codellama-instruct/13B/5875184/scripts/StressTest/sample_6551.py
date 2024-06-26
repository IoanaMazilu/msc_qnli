premise_speed_west = 4
premise_speed_east = 1
hypothesis_speed_west = 3
hypothesis_speed_east = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if hypothesis_speed_west <= premise_speed_west and hypothesis_speed_east <= premise_speed_east:
    # check if the estimate of 'hypothesis_speed_west' and 'hypothesis_speed_east' contradicts the speed of the birds in the premise
    label = "contradiction"
elif hypothesis_speed_west == premise_speed_west and hypothesis_speed_east == premise_speed_east:
    # check if the hypothesis values and estimates do not contradict the premise ones, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
