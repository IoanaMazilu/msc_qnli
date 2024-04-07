# Premise: Two birds start flying simultaneously towards one another, the first leaving from West-Town at a speed of less than 7 kilometers per minute and the second bird, leaving from East-Town, at a speed of 1 kilometers per minute.
# Hypothesis: Two birds start flying simultaneously towards one another, the first leaving from West-Town at a speed of 4 kilometers per minute and the second bird, leaving from East-Town, at a speed of 1 kilometers per minute.
# Golden Label: neutral

west_town_bird_speed_premise = 7
west_town_bird_speed_hypothesis = 4
east_town_bird_speed_premise = 1
east_town_bird_speed_hypothesis = 1

# the hypothesis refers to the speeds of two birds mentioned in the premise
if west_town_bird_speed_hypothesis >= west_town_bird_speed_premise:
    # check if the speed of the bird from West-Town in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif east_town_bird_speed_hypothesis != east_town_bird_speed_premise:
    # check if the speed of the bird from East-Town in the hypothesis contradicts the speed mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

