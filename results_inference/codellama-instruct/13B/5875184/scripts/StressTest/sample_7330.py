premise_red = 3
premise_green = 3
premise_blue = 1

hypothesis_red = 4
hypothesis_green = 3
hypothesis_blue = 1

# the hypothesis refers to the ratio of red, green, and blue bricks used in the tower
if hypothesis_red / hypothesis_green > premise_red / premise_green:
    # check if the hypothesis value contradicts the estimate of more than 'premise_red / premise_green'
    label = "contradiction"
elif hypothesis_blue < premise_blue:
    # check if the hypothesis value contradicts the estimate of 'premise_blue'
    label = "contradiction"
else:
    # the premise gives only an estimate for the ratio of red, green, and blue bricks used in the tower
    # any ratio greater than 'premise_red / premise_green' and 'premise_blue' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
