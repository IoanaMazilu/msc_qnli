speed_west_premise = 7
speed_west_hypothesis = 4
speed_east_premise = 1
speed_east_hypothesis = 1

# the hypothesis refers to the speeds of the birds mentioned in the premise
if speed_west_hypothesis >= speed_west_premise:
    # check if the speed of the bird leaving from West-Town in the hypothesis contradicts the premise
    label = "contradiction"
elif speed_east_hypothesis!= speed_east_premise:
    # check if the speed of the bird leaving from East-Town in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an upper limit for the speed of the bird leaving from West-Town
    # any speed less than'speed_west_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
