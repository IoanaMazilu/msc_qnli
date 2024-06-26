money_given_premise = 40
money_given_hypothesis = 70

# the hypothesis talks about the percentage of money given by Jones, referenced also in the premise
if money_given_hypothesis <= money_given_premise:
    # check if the hypothesis value contradicts the estimate of less than'money_given_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of money given
    # any percentage greater than'money_given_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
