amar_age_premise = 18
akbar_age_premise = 20
anthony_age_premise = 17

# define variables for the hypothesis
amar_age_hypothesis = 21
akbar_age_hypothesis = 22
anthony_age_hypothesis = 19

# calculate the total of the ages in the premise
total_ages_premise = amar_age_premise + akbar_age_premise + anthony_age_premise

# calculate the total of the ages in the hypothesis
total_ages_hypothesis = amar_age_hypothesis + akbar_age_hypothesis + anthony_age_hypothesis

# check if the hypothesis total is more than the premise total
if total_ages_hypothesis > total_ages_premise:
    # the hypothesis contradicts the premise
    label = "contradiction"
elif total_ages_hypothesis <= total_ages_premise:
    # the hypothesis is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # the hypothesis value is not consistent with the premise value
    label = "entailment"

print(label)
