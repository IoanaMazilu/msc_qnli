birds_speed_west_town_premise = 7
birds_speed_west_town_hypothesis = 4
birds_speed_east_town_premise = 1
birds_speed_east_town_hypothesis = 1

# the hypothesis talks about the speed of the birds in West-Town and East-Town
if birds_speed_west_town_hypothesis <= birds_speed_west_town_premise:
    # check if the hypothesis speed in West-Town contradicts the premise speed
    label = "contradiction"
elif birds_speed_east_town_hypothesis!= birds_speed_east_town_premise:
    # check if the hypothesis speed in East-Town contradicts the premise speed
    label = "contradiction"
else:
    # if the hypothesis speeds in West-Town and East-Town do not contradict the premise speeds, we can infer entailment
    label = "entailment"

print(label)
