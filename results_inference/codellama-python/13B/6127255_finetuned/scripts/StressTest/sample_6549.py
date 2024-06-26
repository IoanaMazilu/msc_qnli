bird_speed_west_premise = 4
bird_speed_west_hypothesis = 7
bird_speed_east_premise = 1
bird_speed_east_hypothesis = 1

# the hypothesis refers to the speed of birds leaving from West-Town and East-Town, mentioned in the premise
if bird_speed_west_premise > bird_speed_west_hypothesis:
    # check if the speed of bird leaving from West-Town in the premise contradicts the estimate of less than 'bird_speed_west_hypothesis'
    label = "contradiction"
elif bird_speed_east_hypothesis!= bird_speed_east_premise:
    # check if the speed of bird leaving from East-Town in the hypothesis contradicts the speed of bird leaving from East-Town in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
