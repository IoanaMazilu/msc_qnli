# Premise: In how many years will the benefit Janet receives from her work double given that she receives a simple interest of 10% per annum on the initial agreed paid benefit.
# Hypothesis: In how many years will the benefit Janet receives from her work double given that she receives a simple interest of less than 80% per annum on the initial agreed paid benefit.
# Golden Label: entailment

interest_rate_premise = 10
interest_rate_hypothesis = 80

# the hypothesis refers to the interest rate mentioned in the premise
if interest_rate_hypothesis > interest_rate_premise:
    # check if the estimate of 'interest_rate_hypothesis' contradicts the interest rate in the premise
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we cannot infer entailment, only neutrality
    label = "neutral"

print(label)

