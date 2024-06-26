premise_red = 4
premise_green = 3
premise_blue = 1

hypothesis_red = 8
hypothesis_green = 3
hypothesis_blue = 1

# the hypothesis talks about the ratio of red, green, and blue toy bricks used in the tower
if hypothesis_red < premise_red:
    # check if the hypothesis value contradicts the estimate of more than 'premise_red'
    label = "contradiction"
elif hypothesis_green < premise_green:
    # check if the hypothesis value contradicts the estimate of more than 'premise_green'
    label = "contradiction"
elif hypothesis_blue < premise_blue:
    # check if the hypothesis value contradicts the estimate of more than 'premise_blue'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue toy bricks used in the tower
    # any ratio of red, green, and blue toy bricks greater than 'premise_red', 'premise_green', and 'premise_blue' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
