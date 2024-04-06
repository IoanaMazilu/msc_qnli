# Premise: Mike joined his school's band and he bought a trumpet for $145.16, and sold a song book which was $5.84.
# Hypothesis: The net amount that Mike spent at the music store is 139.32.
# Golden Label: entailment

trumpet_price_premise = 145.16
song_book_price_premise = 5.84
net_spent_hypothesis = 139.32

# the hypothesis refers to the net amount spent by Mike, which can be computed from the premise
# compute the net amount spent in the premise
net_spent_premise = trumpet_price_premise - song_book_price_premise

if net_spent_hypothesis != net_spent_premise:
    # check if the net amount spent in the hypothesis contradicts the net amount spent from the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"    

print(label)
