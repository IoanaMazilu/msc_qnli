# Premise: Renu can do a piece of work in more than 3 days, but with the help of her friend Suma, she can do it in 4 days.
# Hypothesis: Renu can do a piece of work in 5 days, but with the help of her friend Suma, she can do it in 4 days.
# Golden Label: neutral

work_time_renu_premise = 3
work_time_renu_suma_premise = 4
work_time_renu_hypothesis = 5
work_time_renu_suma_hypothesis = 4

# the hypothesis refers to the time Renu takes to do a piece of work, both alone and with the help of Suma, mentioned also in the premise
if work_time_renu_hypothesis <= work_time_renu_premise:
    # check if 'work_time_renu_hypothesis' contradicts the premise's estimate of more than 'work_time_renu_premise' days
    label = "contradiction"
elif work_time_renu_suma_hypothesis != work_time_renu_suma_premise:
    # check if the time Renu and Suma take to do the work together in the hypothesis contradicts the same time reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

