premise_shirts = 40
hypothesis_shirts = 80

# the hypothesis talks about the average number of shirts with Salman, Ambani, and Dalmiya
# if all of them reached a shopping mall in Delhi and purchased 8 shirts each of them
if hypothesis_shirts <= premise_shirts:
    # check if the hypothesis value contradicts the estimate of more than 'premise_shirts'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of shirts
    # any number of shirts greater than 'premise_shirts' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
