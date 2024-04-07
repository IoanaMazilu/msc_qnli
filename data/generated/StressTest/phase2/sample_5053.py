# Premise: Ravina can do the same work in less than 62 days while Gitika can do it in 32 days.
# Hypothesis: Ravina can do the same work in 12 days while Gitika can do it in 32 days.
# Golden Label: neutral

ravina_work_days_premise = 62
ravina_work_days_hypothesis = 12
gitika_work_days_premise = 32
gitika_work_days_hypothesis = 32

# the hypothesis talks about the number of days Ravina and Gitika can finish the work, which is also mentioned in the premise
if ravina_work_days_hypothesis >= ravina_work_days_premise:
    # check if the number of days Ravina can finish the work in the hypothesis contradicts the estimate of less than 'ravina_work_days_premise'
    label = "contradiction"
elif gitika_work_days_hypothesis != gitika_work_days_premise:
    # check if the number of days Gitika can finish the work in the hypothesis contradicts the number of days reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the number of days Ravina can finish the work
    # any number of days less than 'ravina_work_days_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

