years_after_premise = 4
age_after_years_premise = 34
years_after_hypothesis = 6
age_after_years_hypothesis = 34

# the hypothesis talks about the age of Sandy after a certain number of years, referenced also in the premise
if years_after_hypothesis <= years_after_premise and age_after_years_hypothesis == age_after_years_premise:
    # check if the hypothesis value contradicts the estimate of more than 'years_after_premise'
    label = "contradiction"
elif years_after_hypothesis > years_after_premise and age_after_years_hypothesis == age_after_years_premise:
    # the premise gives only an estimate for the number of years
    # any number of years greater than 'years_after_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
