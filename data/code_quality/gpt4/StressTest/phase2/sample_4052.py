sacha_speed_premise = 8
bruno_speed_premise = 5
sacha_speed_hypothesis = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the running speeds of Sacha and Bruno mentioned in the premise
if sacha_speed_hypothesis != sacha_speed_premise:
    # check if the speed of Sacha in the hypothesis contradicts the speed of Sacha reported in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we have either entailment or neutral
    label = "entailment"

print(label)
