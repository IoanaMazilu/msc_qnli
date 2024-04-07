# Premise: James celebrated his 23 rd Birthday on 2016 but he was strangely born in 1950.
# Hypothesis: James celebrated his more than 23 rd Birthday on 2016 but he was strangely born in 1950.
# Golden Label: contradiction

birth_year = 1950
celebration_year_premise = 2016
celebration_year_hypothesis = 2016
birthday_premise = 23
birthday_hypothesis = 23

# the hypothesis refers to the same birth and celebration years mentioned in the premise, and also to the birthday
if birthday_premise >= birthday_hypothesis:
    # check if the estimate of 'birthday_hypothesis' contradicts the birthday number in the premise
    label = "contradiction"
elif celebration_year_premise != celebration_year_hypothesis or birth_year != 1950:
    # check if the years mentioned in the hypothesis contradict the ones in the premise
    label = "contradiction"
else:
    # the premise gives only an exact number for the birthday
    # any birthday number greater than 'birthday_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

