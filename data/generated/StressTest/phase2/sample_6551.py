# Premise: Two birds start flying simultaneously towards one another, the first leaving from West-Town at a speed of 4 kilometers per minute and the second bird, leaving from East-Town, at a speed of 1 kilometers per minute.
# Hypothesis: Two birds start flying simultaneously towards one another, the first leaving from West-Town at a speed of 3 kilometers per minute and the second bird, leaving from East-Town, at a speed of 1 kilometers per minute.
# Golden Label: contradiction

speed_west_town_bird_premise = 4
speed_west_town_bird_hypothesis = 3
speed_east_town_bird_premise = 1
speed_east_town_bird_hypothesis = 1

# the hypothesis refers to the speed of two birds mentioned in the premise
if speed_west_town_bird_hypothesis != speed_west_town_bird_premise:
    # check if the speed of the bird from West-Town in the hypothesis contradicts the speed of the bird from West-Town in the premise
    label = "contradiction"
elif speed_east_town_bird_hypothesis != speed_east_town_bird_premise:
    # check if the speed of the bird from East-Town in the hypothesis contradicts the speed of the bird from East-Town in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

