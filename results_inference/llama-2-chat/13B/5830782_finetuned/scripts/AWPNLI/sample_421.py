trumpet_price_premise = 145.16
song_book_price_premise = 5.84
net_spent_hypothesis = 134.7

# the hypothesis refers to the net amount spent by Mike, which is also mentioned in the premise
# compute the net amount spent in the premise
net_spent_premise = trumpet_price_premise - song_book_price_premise
if net_spent_hypothesis!= net_spent_premise:
    # check if the net amount spent in the hypothesis contradicts the net amount spent from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
