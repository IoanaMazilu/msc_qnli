salary_saving_percentage_premise = 32
salary_saving_percentage_hypothesis = 52

# the hypothesis refers to the percentage of salary Aamir saves, also mentioned in the premise
if salary_saving_percentage_premise >= salary_saving_percentage_hypothesis:
    # check if the premise value contradicts the estimate of less than 'salary_saving_percentage_hypothesis'
    label = "contradiction"
else:
    # the premise gives the exact percentage of salary Aamir saves
    # any percentage less than 'salary_saving_percentage_hypothesis' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
