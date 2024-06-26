days_to_save_premise = 80
days_to_save_hypothesis = 30
salary_per_day = 125

# the hypothesis talks about the number of days Lexi needed to save and the salary per day, both referenced in the premise
if days_to_save_hypothesis >= days_to_save_premise:
    # check if the hypothesis value contradicts the estimate of less than 'days_to_save_premise'
    label = "contradiction"
elif days_to_save_hypothesis < days_to_save_premise:
    # the premise gives only an estimate for the number of days
    # any number of days less than 'days_to_save_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
