avg_price_premise = 12
avg_price_hypothesis = 32

# the hypothesis talks about the average price of the remaining packets, as the premise
if avg_price_premise >= avg_price_hypothesis:
    # check if the premise average price contradicts the hypothesis estimate of less than 'avg_price_hypothesis'
    label = "contradiction"
elif avg_price_premise != avg_price_hypothesis:
    # if the premise average price does not contradict the hypothesis estimate, but also does not match it
    # we can infer neutrality
    label = "neutral"
else:
    # if the premise average price matches the hypothesis estimate, we can infer entailment
    label = "entailment"

print(label)
