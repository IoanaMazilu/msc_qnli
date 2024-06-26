# define variables for the premise and hypothesis
nhai_employees_premise = float(input("Premise: How many more employees should NHAI hire to finish it in time working 10 hours a day? "))
nhai_employees_hypothesis = float(input("Hypothesis: How many more employees should NHAI hire to finish it in time working 70 hours a day? "))

# compare the values of the variables
if nhai_employees_hypothesis <= nhai_employees_premise:
    # check if the hypothesis value contradicts the estimate of the premise
    label = "contradiction"
elif nhai_employees_hypothesis / nhai_employees_premise > 1.5:
    # check if the number of employees in the hypothesis is more than 50% higher than the estimate in the premise
    label = "entailment"
else:
    # if the hypothesis value and estimate do not contradict each other, we can infer neutrality
    label = "neutral"

print(label)
