mac_more_than_ken_premise = 3
mac_more_than_ken_hypothesis = 5
ken_money_increase_premise = 2
ken_money_increase_hypothesis = 2

# the hypothesis refers to the initial and final money amounts for Mac and Ken, mentioned in the premise
if mac_more_than_ken_hypothesis >= mac_more_than_ken_premise:
    # check if the 'mac_more_than_ken_hypothesis' contradicts the initial difference in the premise
    label = "contradiction"
elif ken_money_increase_premise != ken_money_increase_hypothesis:
    # check if the hypothesis value of Ken's increased money contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
