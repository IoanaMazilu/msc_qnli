# Premise: Renu can do a piece of work in 6 days, but with the help of her friend Suma, she can do it in 5 days.
# Hypothesis: Renu can do a piece of work in more than 5 days, but with the help of her friend Suma, she can do it in 5 days.
# Golden Label: entailment

work_days_renu_premise = 6
work_days_renu_and_suma_premise = 5
work_days_renu_hypothesis = 5
work_days_renu_and_suma_hypothesis = 5

# the hypothesis refers to the number of days Renu and Renu with Suma can do a piece of work, mentioned in the premise
if work_days_renu_premise != work_days_renu_hypothesis:
    # check if the number of days Renu can do a piece of work in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
elif work_days_renu_and_suma_hypothesis != work_days_renu_and_suma_premise:
    # check if the number of days Renu and Suma can do a piece of work in the hypothesis contradicts the number of days mentioned in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

