invested_amount_premise = 100000
invested_amount_hypothesis = 600000
interest_rate_premise = 10
interest_rate_hypothesis = 10
period_premise = 3
period_hypothesis = 3

# the hypothesis talks about a smaller investment amount and lower interest rate than the premise
if invested_amount_hypothesis <= invested_amount_premise:
    # check if the hypothesis value contradicts the estimate of more than 'invested_amount_premise'
    label = "contradiction"
elif interest_rate_hypothesis!= interest_rate_premise:
    # check if the hypothesis interest rate contradicts the premise interest rate
    label = "contradiction"
else:
    # the premise gives only an estimate for the investment amount and interest rate
    # any investment amount and interest rate combination greater than the premise values is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
