west_town_speed = 4
east_town_speed = 1
hypothetical_west_town_speed = 3
hypothetical_east_town_speed = 1

# the hypothesis refers to the speed of the birds leaving from West-Town and East-Town
if west_town_speed!= hypothetical_west_town_speed:
    # check if the speed of the bird leaving from West-Town in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
elif east_town_speed!= hypothetical_east_town_speed:
    # check if the speed of the bird leaving from East-Town in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the speeds in the hypothesis do not contradict the speeds in the premise, we can infer entailment
    label = "entailment"

print(label)
