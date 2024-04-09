premise_income = "UK Disposable Income Falls Most In Peacetime Since 1921."
hypothesis_income = "UK disposable income falls to lowest since 1921."

# define variables with representative names for the numerical entities in both inputs
income_premise = float(premise_income.split(" ")[1])
income_hypothesis = float(hypothesis_income.split(" ")[1])

# compare the variables
if income_premise!= income_hypothesis:
    # check if the numerical value in the hypothesis contradicts the premise
    label = "contradiction"
elif income_hypothesis < income_premise:
    # check if the numerical value in the hypothesis is less than the premise
    label = "contradiction"
else:
    # if the numerical value in the hypothesis is greater than or equal to the premise, the hypothesis is neutral
    label = "neutral"

print(label)
