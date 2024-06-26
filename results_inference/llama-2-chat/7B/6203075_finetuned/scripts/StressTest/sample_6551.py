bird_speed_premise_west = 4
bird_speed_premise_east = 1
bird_speed_hypothesis_west = 3
bird_speed_hypothesis_east = 1

# the hypothesis refers to the speed of the birds mentioned in the premise
if bird_speed_premise_west!= bird_speed_hypothesis_west or bird_speed_premise_east!= bird_speed_hypothesis_east:
    # check if the speed of the birds in the hypothesis contradicts the speed of the birds in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
