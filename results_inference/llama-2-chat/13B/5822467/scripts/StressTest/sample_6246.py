investment_premise = 100000
interest_rate_premise = 10
period_premise = 3

investment_hypothesis = 600000

# define variables with representative names for the numerical entities in both inputs
investment_premise_var = var("investment_premise")
interest_rate_premise_var = var("interest_rate_premise")
period_premise_var = var("period_premise")

investment_hypothesis_var = var("investment_hypothesis")

# extract all quantities as valid numbers (integers or floats)
investment_premise_num = float(investment_premise)
interest_rate_premise_num = float(interest_rate_premise)
period_premise_num = float(period_premise)

investment_hypothesis_num = float(investment_hypothesis)

# perform calculations if necessary
interest_hypothesis = investment_hypothesis_num * interest_rate_premise_num * period_premise_num

# compare the variables
if investment_premise_num <= investment_hypothesis_num:
    # check if the estimate of 'investment_hypothesis_num' contradicts the number of investment reported in the premise
    label = "contradiction"
elif interest_hypothesis!= period_premise_num:
    # check if the number of years in the hypothesis contradicts the number of years reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
