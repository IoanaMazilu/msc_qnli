socks_premise = 35
socks_hypothesis = 15

# the hypothesis talks about the number of pairs of matched socks Angela has, which is also mentioned in the premise
if socks_hypothesis >= socks_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # the hypothesis value is less than the premise value, so it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
