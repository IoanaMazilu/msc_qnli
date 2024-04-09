# define variables with representative names for the numerical entities in both inputs
lucy_deposit_premise = 62500
lucy_deposit_hypothesis = float(input("Enter the amount less than $62500: "))

# extract all quantities as valid numbers (integers or floats)
return_premise = 8 * 4 * lucy_deposit_premise / 100
return_hypothesis = 8 * 4 * lucy_deposit_hypothesis / 100

# compare the variables
if lucy_deposit_hypothesis > lucy_deposit_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif lucy_deposit_hypothesis <= lucy_deposit_premise:
    # the hypothesis does not contradict the premise, but cannot be fully and explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is less than the premise value, so we can infer entailment
    label = "entailment"

print(label)
