amar_age = 25
akbar_age = 30
anthony_age = 16

total_ages_premise = amar_age + akbar_age + anthony_age
total_ages_hypothesis = 66

if total_ages_hypothesis <= total_ages_premise:
    # check if the hypothesis value contradicts the estimate of less than 86 years
    label = "contradiction"
elif total_ages_hypothesis > total_ages_premise:
    # check if the hypothesis value entails the premise
    label = "entailment"
else:
    # the premise gives only an estimate for the total ages
    # any value less than 86 years is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
