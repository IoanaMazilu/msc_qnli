# Premise: If, five years from now, the sum W of their ages will be less than 71, how old is Stephanie?
# Hypothesis: If, five years from now, the sum W of their ages will be 51, how old is Stephanie?
# Golden Label: neutral

sum_ages_premise = 71
sum_ages_hypothesis = 51

# the hypothesis refers to the same sum of ages as the premise
if sum_ages_hypothesis >= sum_ages_premise:
    # check if the hypothesis value contradicts the premise estimate of less than 'sum_ages_premise'
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise one, it does not contradict the premise
    # but it cannot be explicitly entailed from the premise, as the premise gives an upper limit, not an exact value
    label = "neutral"

print(label)

