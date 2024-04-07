# Premise: Dana borrows more than 4500 pounds annually for her college education.
# Hypothesis: Dana borrows 7500 pounds annually for her college education.
# Golden Label: neutral

borrowed_pounds_premise = 4500
borrowed_pounds_hypothesis = 7500

# the hypothesis talks about the amount of money Dana borrows annually for her education, referenced also in the premise
if borrowed_pounds_hypothesis <= borrowed_pounds_premise:
    # check if the hypothesis value contradicts the estimate of more than 'borrowed_pounds_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the amount of money Dana borrows
    # any amount greater than 'borrowed_pounds_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

