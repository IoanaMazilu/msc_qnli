# Premise: In how many years will the benefit Janet receives from her work double given that she receives a simple interest of 10% per annum on the initial agreed paid benefit.
# Hypothesis: In how many years will the benefit Janet receives from her work double given that she receives a simple interest of less than 10% per annum on the initial agreed paid benefit.
# Golden Label: contradiction

interest_rate_premise = 10
interest_rate_hypothesis = 10

# the hypothesis talks about the interest rate Janet receives, which is also mentioned in the premise
if interest_rate_hypothesis >= interest_rate_premise:
    # check if the hypothesis value contradicts the premise, which mentions less than 'interest_rate_premise'
    label = "contradiction"
else:
    # the premise gives a specific interest rate
    # any interest rate less than 'interest_rate_premise' does not contradict the premise, but it cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

