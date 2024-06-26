mac_ken_difference_premise = 3
mac_ken_difference_hypothesis = 3
ken_wins_premise = 2
ken_wins_hypothesis = 2

# the hypothesis talks about the amount of money Mac and Ken had, referenced also in the premise
if mac_ken_difference_hypothesis > mac_ken_difference_premise:
    # check if the difference in money between Mac and Ken in the hypothesis contradicts the difference in the premise
    label = "contradiction"
elif ken_wins_hypothesis != ken_wins_premise:
    # check if the amount of money Ken wins in the hypothesis contradicts the amount of money Ken wins in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
