# Define variables for the numerical entities in the premise and hypothesis
premise_ramesh_days = 60
premise_sushil_days = 25
hypothesis_ramesh_days = 20
hypothesis_sushil_days = 25

# Check if the hypothesis values contradict the premise
if hypothesis_ramesh_days > premise_ramesh_days:
    label = "contradiction"
elif hypothesis_sushil_days > premise_sushil_days:
    label = "contradiction"
else:
    label = "neutral"

print(label)
