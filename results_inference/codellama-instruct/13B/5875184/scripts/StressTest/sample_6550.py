premise_speed_west = 7
premise_speed_east = 1
hypothesis_speed_west = 4
hypothesis_speed_east = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if hypothesis_speed_west < premise_speed_west:
    # check if the estimate of 'hypothesis_speed_west' contradicts the speed of the bird leaving from West-Town in the premise
    label = "contradiction"
elif hypothesis_speed_east!= premise_speed_east:
    # check if the speed of the bird leaving from East-Town in the hypothesis contradicts the speed of the bird leaving from East-Town in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
