# Define variables with representative names for the numerical entities in both inputs
ramesh_work_days_premise = 20
sushil_work_days_premise = 25
ramesh_work_days_hypothesis = 20
sushil_work_days_hypothesis = 25

# Extract all quantities as valid numbers (integers or floats)
ramesh_work_days_premise = int(ramesh_work_days_premise)
sushil_work_days_premise = int(sushil_work_days_premise)
ramesh_work_days_hypothesis = int(ramesh_work_days_hypothesis)
sushil_work_days_hypothesis = int(sushil_work_days_hypothesis)

# Use brief comments to explain what comparison you do between the defined variables
if ramesh_work_days_hypothesis <= ramesh_work_days_premise:
    # Check if the estimate of 'ramesh_work_days_hypothesis' contradicts the number of days it takes for Ramesh to finish a work in the premise
    label = "contradiction"
elif sushil_work_days_hypothesis!= sushil_work_days_premise:
    # Check if the number of days it takes for Sushil to finish a work in the hypothesis contradicts the number of days it takes for Sushil to finish a work in the premise
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
