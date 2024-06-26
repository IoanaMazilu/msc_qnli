returned_chocolate_premise = 4
avg_price_remaining_premise = 2
returned_chocolate_hypothesis = 4
avg_price_remaining_hypothesis = 4

# the hypothesis and premise both talk about the number of chocolates returned and the average price of remaining chocolates
if returned_chocolate_premise != returned_chocolate_hypothesis:
    # check if the number of returned chocolates in the hypothesis contradicts the number of returned chocolates reported in the premise
    label = "contradiction"
elif avg_price_remaining_premise != avg_price_remaining_hypothesis:
    # check if the average price of remaining chocolates in the hypothesis contradicts the average price of remaining chocolates in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones
    # but since there's no information about the price of returned chocolates in both premise and hypothesis, we cannot infer entailment
    label = "neutral"

print(label)
