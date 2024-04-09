want_to_give_premise = 95
want_to_give_hypothesis = 55

# the hypothesis talks about the amount of money given to John, referenced also in the premise
if want_to_give_hypothesis <= want_to_give_premise:
    # check if the hypothesis value contradicts the estimate of 'want_to_give_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money to be given
    # any amount of money greater than 'want_to_give_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
