hourly_wage_premise = float(input("Premise: "))
hourly_wage_hypothesis = float(input("Hypothesis: "))

# the hypothesis talks about the hourly wage for a certain number of hours worked, referenced also in the premise
if hourly_wage_hypothesis <= hourly_wage_premise:
    # check if the hypothesis value contradicts the estimate of the hourly wage in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the hourly wage
    # any hourly wage greater than the estimate in the premise is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
