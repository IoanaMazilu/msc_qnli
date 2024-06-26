percentage_died_premise = 15
percentage_died_hypothesis = 85
percentage_left_premise = 25
percentage_left_hypothesis = 25

# the hypothesis talks about the percentage of people died and left in a village, referenced also in the premise
if percentage_died_hypothesis < percentage_died_premise:
    # check if the hypothesis value contradicts the estimate of 'percentage_died_premise' people died
    label = "contradiction"
elif percentage_left_hypothesis != percentage_left_premise:
    # check if the percentage of people left in the hypothesis contradicts the percentage of people left reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
