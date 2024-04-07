# Premise: If, five years from now, the sum R of their ages will be less than 81, how old is Stephanie?
# Hypothesis: If, five years from now, the sum R of their ages will be 51, how old is Stephanie?
# Golden Label: neutral

age_sum_premise = 81
age_sum_hypothesis = 51

# the hypothesis also refers to the sum of their ages, five years from now
if age_sum_hypothesis >= age_sum_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'age_sum_premise'
    label = "contradiction"
else:
    # the premise gives only an estimate for the sum of their ages
    # any sum of ages less than 'age_sum_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

