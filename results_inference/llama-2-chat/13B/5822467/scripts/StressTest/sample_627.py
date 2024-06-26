sock_premise = 10
sock_hypothesis = 70

# the hypothesis refers to the number of pairs of matched socks
if sock_hypothesis <= sock_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # the premise gives a specific value for the number of pairs of matched socks
    # any number of pairs of socks less than 10 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
