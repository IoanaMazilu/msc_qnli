white_socks_percentage_premise = 20
white_socks_percentage_hypothesis = 40

# the hypothesis refers to the percentage of white socks in a shop mentioned in the premise
if white_socks_percentage_hypothesis <= white_socks_percentage_premise:
    # check if the hypothesis value contradicts the estimate of more than 'white_socks_percentage_premise'
    label = "contradiction"
else:
    # the premise provides only an estimate for the percentage of white socks
    # any percentage of white socks greater than 'white_socks_percentage_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
