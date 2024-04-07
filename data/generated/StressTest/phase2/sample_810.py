# Premise: Sacha runs at a constant speed of 6 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Hypothesis: Sacha runs at a constant speed of less than 7 meters per second, and Bruno runs at a constant speed of 5 meters per second.
# Golden Label: entailment

sacha_speed_premise = 6
bruno_speed_premise = 5
sacha_speed_hypothesis = 7
bruno_speed_hypothesis = 5

# the hypothesis refers to the running speeds of Sacha and Bruno mentioned in the premise
if sacha_speed_premise >= sacha_speed_hypothesis:
    # check if the hypothesis value contradicts the running speed of Sacha in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the running speed of Bruno in the hypothesis contradicts his running speed reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

