boy_age_premise = 20
boy_age_hypothesis = 80

# the hypothesis talks about the number of boys of different ages in John's School, referenced also in the premise
if boy_age_hypothesis <= boy_age_premise:
    # check if the hypothesis value contradicts the estimate of more than 'boy_age_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of boys of each age
    # any number of boys of each age greater than 'boy_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
