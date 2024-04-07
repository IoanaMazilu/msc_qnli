# Premise: Sacha runs at a constant speed of 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of more than 5 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: entailment

sacha_speed_premise = 6
bruno_speed_premise = 5
sacha_speed_hypothesis = 5
bruno_speed_hypothesis = 5

# The hypothesis refers to the running speed of Sacha and Bruno mentioned in the premise
if sacha_speed_premise <= sacha_speed_hypothesis:
    # Check if the estimate of 'sacha_speed_hypothesis' contradicts the speed of Sacha in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # Check if the speed of Bruno in the hypothesis contradicts the speed of Bruno reported in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

