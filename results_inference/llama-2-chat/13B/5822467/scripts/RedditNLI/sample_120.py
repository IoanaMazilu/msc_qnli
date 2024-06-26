premise_base_rate = "2006"
hypothesis_base_rate = "2008"

# define variables with representative names for the numerical entities in both inputs
base_rate_premise = int(premise_base_rate)
base_rate_hypothesis = int(hypothesis_base_rate)

# extract all quantities as valid numbers (integers or floats)
if base_rate_premise!= base_rate_hypothesis:
    # check if the base rate in the hypothesis contradicts the base rate in the premise
    label = "contradiction"
elif base_rate_hypothesis < base_rate_premise:
    # check if the base rate in the hypothesis contradicts the premise estimate of "2006"
    label = "contradiction"
else:
    # the premise gives only an estimate for the base rate
    # any estimate of the base rate in the hypothesis greater or equal to "2006" is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
