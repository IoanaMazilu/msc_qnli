# Premise: Ravina can do the same work in 12 days while Gitika can do it in 32 days.
# Hypothesis: Ravina can do the same work in 22 days while Gitika can do it in 32 days.
# Golden Label: contradiction

ravina_work_days_premise = 12
gitika_work_days_premise = 32
ravina_work_days_hypothesis = 22
gitika_work_days_hypothesis = 32

# the hypothesis refers to the number of days Ravina and Gitika can do the same work, as mentioned in the premise
if ravina_work_days_hypothesis != ravina_work_days_premise:
    # check if the number of days for Ravina in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
elif gitika_work_days_hypothesis != gitika_work_days_premise:
    # check if the number of days for Gitika in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise ones, we can infer entailment
    label = "neutral"

print(label)

