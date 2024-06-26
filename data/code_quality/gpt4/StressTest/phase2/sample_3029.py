sacha_speed_premise = 10
bruno_speed_premise = 5
sacha_speed_hypothesis = 80
bruno_speed_hypothesis = 5

# the hypothesis refers to the running speed of Sacha and Bruno, as mentioned in the premise
if sacha_speed_premise != sacha_speed_hypothesis:
    # check if the speed of Sacha in the hypothesis contradicts the speed of Sacha reported in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
