number_premise = 8
number_hypothesis = 4

# the hypothesis talks about a number which is less than the square of a positive integer, referenced also in the premise
if number_hypothesis > number_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif number_hypothesis == number_premise:
    # check if the hypothesis value equals the premise value
    label = "entailment"
else:
    # the premise gives only an estimate for the number
    # any number less than 'number_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
