socks_premise = 35
socks_hypothesis = 15

# the hypothesis refers to the number of Angela's socks mentioned in the premise
if socks_hypothesis >= socks_premise:
    # check if the number of socks in the hypothesis contradicts the premise's estimate of less than'socks_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of socks
    # any number of socks less than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)