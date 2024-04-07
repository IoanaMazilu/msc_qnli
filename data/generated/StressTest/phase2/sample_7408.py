# Premise: Sam wrote more than 4 letters on Tuesday and 3 letters on Wednesday.
# Hypothesis: Sam wrote 7 letters on Tuesday and 3 letters on Wednesday.
# Golden Label: neutral

letters_tuesday_premise = 4
letters_tuesday_hypothesis = 7
letters_wednesday_premise = 3
letters_wednesday_hypothesis = 3

# the hypothesis refers to the number of letters written on Tuesday and Wednesday mentioned in the premise
if letters_tuesday_hypothesis <= letters_tuesday_premise:
    # check if the number of letters written on Tuesday in the hypothesis contradicts the estimate of more than 'letters_tuesday_premise'
    label = "contradiction"
elif letters_wednesday_hypothesis != letters_wednesday_premise:
    # check if the number of letters written on Wednesday in the hypothesis contradicts the number of letters written on Wednesday reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of letters written on Tuesday
    # any number of letters greater than 'letters_tuesday_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

