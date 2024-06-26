# define the variables for the premise and hypothesis
distance_traveled_premise = 200
distance_traveled_hypothesis = 200

# the hypothesis refers to the distance traveled on the first day of Louisa's vacation mentioned in the premise
if distance_traveled_premise <= distance_traveled_hypothesis:
    # check if the estimate of 'distance_traveled_hypothesis' contradicts the distance traveled in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)