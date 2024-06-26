white_socks_premise = 40
white_socks_hypothesis = 80

# the hypothesis refers to the percentage of white socks in the premise
if white_socks_hypothesis <= white_socks_premise:
    # check if the estimate of 'white_socks_hypothesis' contradicts the percentage of white socks in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of white socks
    # any percentage of white socks greater than 'white_socks_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
