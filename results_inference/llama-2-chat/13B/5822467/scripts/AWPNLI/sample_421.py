# define variables with representative names for the numerical entities in both inputs
trumpet_price_premise = 145.16
song_book_price_premise = 5.84
net_amount_hypothesis = 134.7

# extract all quantities as valid numbers (integers or floats)
trumpet_price_premise = float(trumpet_price_premise)
song_book_price_premise = float(song_book_price_premise)
net_amount_hypothesis = float(net_amount_hypothesis)

# compare the variables
if net_amount_hypothesis > trumpet_price_premise + song_book_price_premise:
    # the hypothesis entails the premise
    label = "entailment"
elif net_amount_hypothesis < trumpet_price_premise + song_book_price_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
else:
    # the hypothesis and premise have the same value, so there is no contradiction or entailment
    label = "neutral"

print(label)
