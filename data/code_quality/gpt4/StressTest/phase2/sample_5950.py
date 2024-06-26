T_premise = 20
premise_fraction = 2/9
T_hypothesis = 20
hypothesis_fraction = 5/9

# the hypothesis refers to the same variable T as the premise,
# but with a different fraction in the formula for calculating K
if premise_fraction >= hypothesis_fraction:
    # check if the fraction in the premise is greater or equal to the fraction in the hypothesis
    label = "contradiction"
else:
    # the premise gives only an estimate for the fraction in the formula
    # any fraction greater than 'premise_fraction' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
