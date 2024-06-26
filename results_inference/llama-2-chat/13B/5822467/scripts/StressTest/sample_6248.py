investment_premise = 100000
interest_rate_premise = 10
period_premise = 3

investment_hypothesis = float(input("Enter the amount invested: "))
interest_rate_hypothesis = float(input("Enter the interest rate: "))
period_hypothesis = float(input("Enter the period: "))

# Calculate the total amount after 3 years with the given interest rate and period
total_premise = investment_premise * (1 + interest_rate_premise/100)**period_premise
total_hypothesis = investment_hypothesis * (1 + interest_rate_hypothesis/100)**period_hypothesis

# Check if the hypothesis contradicts the premise
if total_hypothesis < total_premise:
    label = "contradiction"
elif total_hypothesis > total_premise:
    label = "entailment"
else:
    label = "neutral"

print(label)
