socks_premise = 6
socks_hypothesis = 2

# the hypothesis talks about the number of socks Barbara wears, which is also referenced in the premise
if socks_hypothesis >= socks_premise:
    # check if the hypothesis value contradicts the premise of less than'socks_premise'
    label = "contradiction"
elif socks_hypothesis < socks_premise:
    # if the hypothesis value is less than the premise value, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise either
    label = "neutral"

print(label)
