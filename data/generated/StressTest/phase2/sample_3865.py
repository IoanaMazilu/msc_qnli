# Premise: Srinivas saves one coin of more than 4 on first day of the week, three coins of 5 on the second day of the week. Five coins of 5 on third day and so on.
# Hypothesis: Srinivas saves one coin of 5 on first day of the week, three coins of 5 on the second day of the week. Five coins of 5 on third day and so on.
# Golden Label: neutral

first_day_coin_value_premise = 4
first_day_coin_value_hypothesis = 5
second_day_coins_premise = third_day_coins_premise = 5
second_day_coins_hypothesis = third_day_coins_hypothesis = 5

# the hypothesis refers to the same pattern of savings mentioned in the premise
if first_day_coin_value_hypothesis <= first_day_coin_value_premise:
    # check if the value of the coin saved on the first day in the hypothesis contradicts the estimate in the premise
    label = "contradiction"
elif second_day_coins_hypothesis != second_day_coins_premise or third_day_coins_hypothesis != third_day_coins_premise:
    # check if the number of coins saved on the second and third day in the hypothesis contradicts the number mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

