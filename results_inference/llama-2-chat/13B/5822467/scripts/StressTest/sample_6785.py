# define variables with representative names for the numerical entities in both inputs
x_premise = 40
x_hypothesis = float("inf")
pay_per_hour_premise = 1.0 * x_premise
pay_per_hour_hypothesis = 1.5 * x_hypothesis

# extract all quantities as valid numbers
# do not ignore any quantity or numerical information

# compare the variables
if pay_per_hour_hypothesis <= pay_per_hour_premise:
    # check if the hypothesis value contradicts the estimate of 'pay_per_hour_premise'
    label = "contradiction"
elif pay_per_hour_hypothesis > pay_per_hour_premise:
    # check if the hypothesis value entails the estimate of 'pay_per_hour_premise'
    label = "entailment"
else:
    # the premise gives only an estimate for the number of hours worked
    # any number of hours worked greater than 'pay_per_hour_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
