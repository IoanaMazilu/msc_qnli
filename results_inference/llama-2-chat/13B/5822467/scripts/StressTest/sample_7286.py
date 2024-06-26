# Define variables with representative names for the numerical entities in both inputs
commission_premise = 15
commission_hypothesis = 55
job_pay_premise = 75000
job_pay_hypothesis = 45000

# Extract all quantities as valid numbers (integers or floats)
commission_premise = int(commission_premise)
commission_hypothesis = int(commission_hypothesis)
job_pay_premise = int(job_pay_premise)
job_pay_hypothesis = int(job_pay_hypothesis)

# Perform calculations if necessary
total_commission_premise = commission_premise * job_pay_premise
total_commission_hypothesis = commission_hypothesis * job_pay_hypothesis

# Compare the variables and infer a label
if job_pay_hypothesis > job_pay_premise:
    # The hypothesis states that John left a job paying more than $75,000 per year, which contradicts the premise.
    label = "contradiction"
elif commission_hypothesis > commission_premise:
    # The hypothesis states that John left a job paying $45,000 per year plus a higher commission, which entails the premise.
    label = "entailment"
else:
    # The hypothesis values and estimates do not contradict the premise ones, so we can infer neutrality.
    label = "neutral"

print(label)
