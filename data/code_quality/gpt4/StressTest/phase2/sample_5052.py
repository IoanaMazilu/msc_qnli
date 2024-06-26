ravina_work_days_premise = 12
ravina_work_days_hypothesis = 62
gitika_work_days_premise = 32
gitika_work_days_hypothesis = 32

# the hypothesis refers to the number of days Ravina and Gitika can complete the work in, mentioned in the premise
if ravina_work_days_hypothesis < ravina_work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise for Ravina
    label = "contradiction"
elif gitika_work_days_hypothesis != gitika_work_days_premise:
    # check if the number of work days in the hypothesis contradicts the number of work days reported in the premise for Gitika
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
