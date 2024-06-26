# defining the average speed of Murali from A to C given the ratio of distances between A to B and B to C
average_speed_premise = 4 / 2

# defining the average speed of Murali from A to C given the ratio of distances between A to B and B to C in the hypothesis
average_speed_hypothesis = 1 / 2

# comparing the average speed of Murali from A to C in the premise and the hypothesis
if average_speed_premise <= average_speed_hypothesis:
    # if the average speed of Murali from A to C in the premise is less than or equal to the average speed in the hypothesis, we have a contradiction
    label = "contradiction"
elif average_speed_premise > average_speed_hypothesis:
    # if the average speed of Murali from A to C in the premise is greater than the average speed in the hypothesis, we have entailment
    label = "entailment"
else:
    # if the average speed of Murali from A to C in the premise is neither less than nor greater than the average speed in the hypothesis, we have neutral
    label = "neutral"

print(label)
