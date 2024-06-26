loss_premise = 0
loss_hypothesis = 0
years_premise = 2
years_hypothesis = 6
interest_rate_premise = 4
interest_rate_hypothesis = 4

# the hypothesis talks about the number of years and interest rate for the loss calculation, referenced also in the premise
if years_hypothesis <= years_premise:
    # check if the hypothesis value contradicts the number of years in the premise
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the interest rate in the hypothesis contradicts the interest rate reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of years and the interest rate
    # any number of years and interest rate consistent with the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
