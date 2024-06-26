sacha_speed_premise = 80
sacha_speed_hypothesis = 10
bruno_speed_premise = 5
bruno_speed_hypothesis = 5

# the hypothesis refers to the speed of Sacha and Bruno, mentioned also in the premise
if sacha_speed_hypothesis >= sacha_speed_premise:
    # check if the estimate of 'sacha_speed_hypothesis' contradicts the speed limit in the premise
    label = "contradiction"
elif bruno_speed_hypothesis != bruno_speed_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno reported in the premise
    label = "contradiction"
elif sacha_speed_hypothesis > sacha_speed_premise:
    # check if Sacha's speed in the hypothesis is greater than the speed of Sacha reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
