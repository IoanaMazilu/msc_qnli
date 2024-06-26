less_than_6600 = 6600

# the hypothesis talks about the total amount among John, Jose & Binoy, referenced also in the premise
if less_than_6600 >= 6600:
    # check if the hypothesis value contradicts the estimate of less than 'less_than_6600'
    label = "contradiction"
else:
    # the premise gives the exact total amount
    # any total amount less than 'less_than_6600' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
