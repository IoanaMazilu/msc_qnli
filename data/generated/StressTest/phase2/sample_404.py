# Premise: Sacha runs at a constant speed of 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of less than 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: contradiction

sacha_speed_premise = 6
sacha_speed_hypothesis = 6
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the speeds of Sacha and Bruno mentioned in the premise
if sacha_speed_premise != sacha_speed_hypothesis:
    # check if the statement about Sacha's speed in the hypothesis contradicts the speed of Sacha in the premise
    label = "contradiction"
elif bruno_speed_premise != bruno_speed_hypothesis:
    # check if the statement about Bruno's speed in the hypothesis contradicts the speed of Bruno in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

