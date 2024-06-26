sock_premise = 10
sock_hypothesis = 40

# the hypothesis refers to the number of pairs of socks owned by John
if sock_hypothesis <= sock_premise:
    # check if the hypothesis value contradicts the estimate of'sock_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of pairs of socks
    # any number of pairs of socks less than'sock_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
