joined_band_premise = True
bought_trumpet_premise = 145.16
sold_song_book_premise = 5.84
net_amount_hypothesis = 134.7

# the hypothesis refers to the net amount that Mike spent at the music store, which is also mentioned in the premise
# compute the net amount from the premise
net_amount_premise = bought_trumpet_premise - sold_song_book_premise
if net_amount_hypothesis!= net_amount_premise:
    # check if the net amount in the hypothesis contradicts the net amount from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
