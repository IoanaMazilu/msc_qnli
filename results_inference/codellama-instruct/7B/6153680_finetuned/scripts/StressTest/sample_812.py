speed_sacha_premise = 6
speed_sacha_hypothesis = 3
speed_bruno_premise = 5
speed_bruno_hypothesis = 5

# the hypothesis refers to the speed of Sacha and Bruno mentioned in the premise
if speed_sacha_hypothesis!= speed_sacha_premise:
    # check if the speed of Sacha in the hypothesis contradicts the speed of Sacha in the premise
    label = "contradiction"
elif speed_bruno_hypothesis!= speed_bruno_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
