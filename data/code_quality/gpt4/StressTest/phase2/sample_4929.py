earnings_rise_premise = 30
earnings_rise_hypothesis = 40
earnings_amount_premise = 598
earnings_amount_hypothesis = 598

# the hypothesis talks about Albert's monthly earnings and the percentage rise, the same as in the premise
if earnings_rise_hypothesis <= earnings_rise_premise and earnings_amount_hypothesis == earnings_amount_premise:
    # check if the hypothesis percentage rise contradicts the premise percentage rise, and if the earnings amount is the same
    label = "contradiction"
elif earnings_rise_hypothesis > earnings_rise_premise and earnings_amount_hypothesis == earnings_amount_premise:
    # check if the hypothesis percentage rise is larger than the premise percentage rise, and if the earnings amount is the same
    label = "entailment"
else:
    # if the hypothesis values and estimates do not contradict or entail the premise ones, we can infer neutrality
    label = "neutral"

print(label)
