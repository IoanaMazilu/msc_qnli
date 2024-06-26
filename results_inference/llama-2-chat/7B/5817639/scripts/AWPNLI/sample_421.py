joined_band_premise = "Mike joined his school's band"
trumpet_price_premise = $145.16
songbook_price_premise = $5.84
net_amount_hypothesis = 134.7

# the hypothesis talks about the net amount spent at the music store, which is also mentioned in the premise
# compute the total amount spent on the trumpet and the songbook
total_amount_premise = trumpet_price_premise + songbook_price_premise

# compare the hypothesis value with the total amount spent in the premise
if net_amount_hypothesis == total_amount_premise:
    # if the hypothesis value matches the total amount spent in the premise, we can infer entailment
    label = "entailment"
elif net_amount_hypothesis < total_amount_premise:
    # if the hypothesis value is less than the total amount spent in the premise, we can infer contradiction
    label = "contradiction"
else:
    # if the hypothesis value is equal to the total amount spent in the premise, we can infer neutrality
    label = "neutral"

print(label)
