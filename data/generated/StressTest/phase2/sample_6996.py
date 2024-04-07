# Premise: Sacha runs at a constant speed of 9 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of more than 1 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: entailment

sacha_speed_premise = 9
sacha_speed_hypothesis = 1
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the running speeds of Sacha and Bruno, as mentioned in the premise
if sacha_speed_premise <= sacha_speed_hypothesis:
    # check if the estimate of 'sacha_speed_hypothesis' contradicts the Sacha's speed in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the Bruno's speed in the hypothesis contradicts the Bruno's speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

