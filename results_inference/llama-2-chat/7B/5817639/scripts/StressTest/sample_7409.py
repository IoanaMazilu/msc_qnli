letters_tuesday_premise = 7
letters_tuesday_hypothesis = 3
letters_wednesday_premise = 3
letters_wednesday_hypothesis = 3

# the hypothesis talks about the number of letters written on Tuesday and Wednesday, referenced also in the premise
if letters_tuesday_hypothesis <= letters_tuesday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'letters_tuesday_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of letters written on Tuesday
    # any number of letters greater than 'letters_tuesday_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

if letters_wednesday_hypothesis <= letters_wednesday_premise:
    # check if the hypothesis value contradicts the estimate of more than 'letters_wednesday_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of letters written on Wednesday
    # any number of letters greater than 'letters_wednesday_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
