# Premise: Sacha runs at a constant speed of 7 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of less than 7 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: contradiction

sacha_speed_premise = 7
sacha_speed_hypothesis = 7
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis talks about the speed of Sacha and Bruno, both also mentioned in the premise
if sacha_speed_hypothesis >= sacha_speed_premise:
    # check if the estimate of 'sacha_speed_hypothesis' contradicts the speed of Sacha in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

