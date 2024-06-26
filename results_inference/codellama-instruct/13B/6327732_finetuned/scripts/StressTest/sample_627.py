socks_premise = 10
socks_hypothesis = 70

# the hypothesis refers to the number of pairs of socks mentioned in the premise
if socks_premise <= socks_hypothesis:
    # check if the estimate of'socks_hypothesis' contradicts the number of socks in the premise
    label = "contradiction"
else:
    # the premise gives an exact number of socks, but the hypothesis gives an estimate
    # any number of socks greater than'socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
