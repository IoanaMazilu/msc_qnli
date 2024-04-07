# Premise: If, five years from now, the sum Q of their ages will be more than 31, how old is Stephanie?
# Hypothesis: If, five years from now, the sum Q of their ages will be 51, how old is Stephanie?
# Golden Label: neutral

sum_ages_future_premise = 31
sum_ages_future_hypothesis = 51

# the hypothesis refers to the future sum of their ages mentioned in the premise
if sum_ages_future_hypothesis <= sum_ages_future_premise:
    # check if the future sum of their ages in the hypothesis contradicts the future sum of their ages reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the future sum of their ages
    # any future sum of their ages greater than 'sum_ages_future_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

