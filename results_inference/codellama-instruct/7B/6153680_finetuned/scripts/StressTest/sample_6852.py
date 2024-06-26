coin_amount_1 = 2
coin_amount_2 = 5
coin_metal_1 = 'iron'
coin_metal_2 = 'copper'

# the hypothesis refers to the amounts and metals of the coins
# the premise mentions the same amounts and metals
# the hypothesis also mentions that the amounts are less than 3 ¢
if coin_amount_1 >= 3 or coin_amount_2 >= 3:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
