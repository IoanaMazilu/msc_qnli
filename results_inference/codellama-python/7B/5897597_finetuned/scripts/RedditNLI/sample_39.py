current_account_surplus_japan_premise = 0.93
current_account_surplus_south_korea_hypothesis = 7.01

# the hypothesis and premise mention the current account surplus of Japan and South Korea in June of 2017
if current_account_surplus_japan_premise!= current_account_surplus_south_korea_hypothesis:
    # check if the current account surplus of Japan in the hypothesis contradicts the current account surplus of Japan in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
