percentage_white_premise = 40
percentage_white_hypothesis = 80

# the hypothesis refers to a lower percentage of white socks than the premise
if percentage_white_hypothesis <= percentage_white_premise:
    # check if the hypothesis value contradicts the estimate of more than 'percentage_white_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the percentage of white socks, which the hypothesis cannot explicitly entail
    label = "neutral"

print(label)
