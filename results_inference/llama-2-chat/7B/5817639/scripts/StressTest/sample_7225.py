# Define variables for the numerical entities in the premise and hypothesis
oa_premise = float(input("Enter the value of OA in the premise: "))
ac_premise = float(input("Enter the value of AC in the premise: "))
bd_premise = float(input("Enter the value of BD in the premise: "))

oa_hypothesis = float(input("Enter the value of OA in the hypothesis: "))
ac_hypothesis = float(input("Enter the value of AC in the hypothesis: "))
bd_hypothesis = float(input("Enter the value of BD in the hypothesis: "))

# Extract all quantities as valid numbers
oa_hypothesis = oa_hypothesis if oa_hypothesis > 0 else 0
ac_hypothesis = ac_hypothesis if ac_hypothesis > 0 else 0
bd_hypothesis = bd_hypothesis if bd_hypothesis > 0 else 0

# Compare the variables
if oa_hypothesis <= oa_premise:
    # Check if the hypothesis value contradicts the estimate of less than 'oa_premise'
    label = "contradiction"
elif ac_hypothesis!= ac_premise:
    # Check if the hypothesis value contradicts the estimate of 'ac_premise'
    label = "contradiction"
elif bd_hypothesis!= bd_premise:
    # Check if the hypothesis value contradicts the estimate of 'bd_premise'
    label = "contradiction"
else:
    # If the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
