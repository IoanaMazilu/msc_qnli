# Premise: In how many years will the benefit Janet receives from her work double given that she receives a simple interest of less than 80% per annum on the initial agreed paid benefit.
# Hypothesis: In how many years will the benefit Janet receives from her work double given that she receives a simple interest of 10% per annum on the initial agreed paid benefit.
# Golden Label: neutral

interest_rate_premise = 80
interest_rate_hypothesis = 10

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis >= interest_rate_premise:
    # check if the hypothesis value contradicts the estimate of less than 'interest_rate_premise'
    label = "contradiction"
elif interest_rate_hypothesis == interest_rate_premise:
    # check if the interest rate in the hypothesis matches the interest rate in the premise
    label = "entailment"
else:
    # the premise gives only an upper limit for the interest rate
    # any interest rate less than 'interest_rate_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

