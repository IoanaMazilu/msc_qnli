song_price_premise = 0.99
song_price_hypothesis = 0.99

# the hypothesis mentions the cost of each song, which is also mentioned in the premise
if song_price_hypothesis != song_price_premise:
    # check if the song price in the hypothesis contradicts the song price reported in the premise
    label = "contradiction"
else:
    # if the song price in the hypothesis does not contradict the premise, we can infer entailment
    label = "entailment"

print(label)
