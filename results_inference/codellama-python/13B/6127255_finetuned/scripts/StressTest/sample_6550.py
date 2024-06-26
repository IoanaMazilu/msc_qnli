bird_speed_west_premise = 7
bird_speed_west_hypothesis = 4
bird_speed_east_premise = 1
bird_speed_east_hypothesis = 1

# the hypothesis refers to the speed of the birds leaving from West-Town and East-Town, mentioned in the premise
if bird_speed_west_hypothesis >= bird_speed_west_premise:
    # check if the speed of the bird leaving from West-Town in the hypothesis contradicts the premise
    label = "contradiction"
elif bird_speed_east_hypothesis!= bird_speed_east_premise:
    # check if the speed of the bird leaving from East-Town in the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the speed of the bird leaving from West-Town
    # any speed less than 'bird_speed_west_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
