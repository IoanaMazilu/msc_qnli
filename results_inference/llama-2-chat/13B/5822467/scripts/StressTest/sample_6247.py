investment_premise = 600000
investment_hypothesis = 100000
interest_rate = 10
period = 3

# define variables with representative names for the numerical entities in both inputs
investment_premise_label = "less than 600000"
investment_hypothesis_label = "100000"

# extract all quantities as valid numbers (integers or floats)
investment_premise_value = float(investment_premise)
investment_hypothesis_value = float(investment_hypothesis)

# perform calculations if necessary
interest_earned_premise = investment_premise_value * interest_rate * period
interest_earned_hypothesis = investment_hypothesis_value * interest_rate * period

# compare the variables
if investment_premise_value <= investment_hypothesis_value:
    # check if the estimate of 'investment_hypothesis_value' contradicts the value of 'investment_premise_value'
    label = "contradiction"
elif interest_earned_premise!= interest_earned_hypothesis:
    # check if the amount of interest earned in the hypothesis contradicts the amount of interest earned in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
