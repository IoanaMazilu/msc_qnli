yapil_speed_sacha_premise = 1
yapil_speed_sacha_hypothesis = 9
yapil_speed_bruno_premise = 5
yapil_speed_bruno_hypothesis = 5

# the hypothesis talks about the speed of Sacha and Bruno, referenced also in the premise
if yapil_speed_sacha_hypothesis <= yapil_speed_sacha_premise:
    # check if the speed of Sacha in the hypothesis contradicts the speed of Sacha in the premise
    label = "contradiction"
elif yapil_speed_bruno_hypothesis!= yapil_speed_bruno_premise:
    # check if the speed of Bruno in the hypothesis contradicts the speed of Bruno in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
