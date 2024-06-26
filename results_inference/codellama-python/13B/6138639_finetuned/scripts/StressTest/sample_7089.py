money_premise = 1200
money_hypothesis = 3200

# the hypothesis talks about Mary's monthly salary, referenced also in the premise
if money_hypothesis <= money_premise:
    # check if the hypothesis value contradicts the estimate of less than'money_hypothesis'
    label = "contradiction"
else:
    # the premise gives only an estimate for the monthly salary
    # any monthly salary less than'money_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
