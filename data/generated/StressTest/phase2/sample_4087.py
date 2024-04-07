# Premise: Paul's salary was decreased by more than 30% and subsequently increased by 50 %.
# Hypothesis: Paul's salary was decreased by 50% and subsequently increased by 50 %.
# Golden Label: neutral

salary_decrease_premise = 30
salary_increase_premise = 50
salary_decrease_hypothesis = 50
salary_increase_hypothesis = 50

# the hypothesis talks about the percentage of salary decrease and increase referenced also in the premise
if salary_decrease_hypothesis < salary_decrease_premise:
    # check if the hypothesis value contradicts the estimate of more than 'salary_decrease_premise'
    label = "contradiction"
elif salary_increase_hypothesis != salary_increase_premise:
    # check if the percentage of salary increase in the hypothesis contradicts the percentage of salary increase reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the percentage of salary decrease
    # any percentage of salary decrease greater than 'salary_decrease_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

