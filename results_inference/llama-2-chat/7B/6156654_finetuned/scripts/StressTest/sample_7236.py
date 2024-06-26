distance_traveled_premise = 240
distance_traveled_hypothesis = 440

# the hypothesis refers to the distance traveled by Louisa on the first day of her vacation, as mentioned in the premise
if distance_traveled_premise >= distance_traveled_hypothesis:
    # check if the distance traveled in the premise contradicts the hypothesis
    label = "contradiction"
elif distance_traveled_premise < distance_traveled_hypothesis:
    # check if the distance traveled in the premise is less than the one in the hypothesis
    # this is entailed by the hypothesis
    label = "entailment"
else:
    # if the distance traveled in the premise is equal to the one in the hypothesis, we can't infer anything
    label = "neutral"

print(label)
