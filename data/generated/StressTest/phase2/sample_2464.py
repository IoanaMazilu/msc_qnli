# Premise: If Pinky returned four chocolate to the retailer, and the average price of the remaining chocolate was less than 4 ¢, then what is the average price, in cents, of the four returned chocolates?
# Hypothesis: If Pinky returned four chocolate to the retailer, and the average price of the remaining chocolate was 2 ¢, then what is the average price, in cents, of the four returned chocolates?
# Golden Label: neutral

avg_price_remaining_choco_premise = 4
avg_price_remaining_choco_hypothesis = 2

# the hypothesis talks about the average price of remaining chocolates, referenced also in the premise
if avg_price_remaining_choco_hypothesis >= avg_price_remaining_choco_premise:
    # check if the hypothesis value contradicts the estimate of less than 'avg_price_remaining_choco_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the average price of remaining chocolates
    # any average price less than 'avg_price_remaining_choco_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

