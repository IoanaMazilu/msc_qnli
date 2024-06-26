ramesh_days_premise = 20
sushil_days_premise = 25
ramesh_days_hypothesis = float(input("Enter the number of days Ramesh can finish the work: "))
sushil_days_hypothesis = float(input("Enter the number of days Sushil can finish the work: "))

# Check if Ramesh's estimated time contradicts the premise
if ramesh_days_hypothesis > ramesh_days_premise:
    label = "contradiction"
elif sushil_days_hypothesis == sushil_days_premise:
    # No comparison is needed, the hypothesis does not provide any new information
    label = "neutral"
else:
    # Check if the hypothesis values and estimates do not contradict the premise ones
    label = "entailment"

print(label)
