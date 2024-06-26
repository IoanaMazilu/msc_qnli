sandy_age_in_years_after_premise = 34
sandy_age_in_years_later_premise = 6
sandy_age_in_years_after_hypothesis = 34
sandy_age_in_years_later_hypothesis = 4

# the hypothesis talks about Sandy's age after a number of years, the same as the premise
if sandy_age_in_years_after_hypothesis != sandy_age_in_years_after_premise or sandy_age_in_years_later_hypothesis != sandy_age_in_years_later_premise:
    # check if the hypothesis contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
