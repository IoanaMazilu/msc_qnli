mac_ken_difference_premise = 5
mac_ken_difference_hypothesis = 3
ken_new_money_premise = 2
ken_new_money_hypothesis = 2

# the hypothesis talks about the difference in money between Mac and Ken and the new amount of money Ken has after winning on the horses
# both these aspects are also mentioned in the premise
if mac_ken_difference_premise != mac_ken_difference_hypothesis:
    # check if the difference in money between Mac and Ken in the hypothesis contradicts the same difference mentioned in the premise
    label = "contradiction"
elif ken_new_money_premise != ken_new_money_hypothesis:
    # check if the new amount of money Ken has in the hypothesis contradicts the same amount mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
