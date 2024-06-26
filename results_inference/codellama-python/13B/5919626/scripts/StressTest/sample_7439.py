fastest_horses_london = 3
fastest_horses_ky = 4
horses_london = 25
horses_ky = 25

# the hypothesis talks about the number of horses submitted to the Kentucky Derby
# the premise gives an estimate for the number of fastest horses submitted to the Kentucky Derby
if fastest_horses_ky <= fastest_horses_london:
    # check if the hypothesis value contradicts the estimate of more than 'fastest_horses_london'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of fastest horses
    # any number of fastest horses greater than 'fastest_horses_london' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
