birthday_year_premise = 23 
birthday_year_hypothesis = 43 
birth_year_premise = 1950
birth_year_hypothesis = 1950

# the hypothesis refers to the birthday year and birth year mentioned in the premise
if birthday_year_hypothesis >= birthday_year_premise:
    # check if the estimate of 'birthday_year_hypothesis' contradicts the birthday year in the premise
    label = "contradiction"
elif birth_year_hypothesis != birth_year_premise:
    # check if the birth year in the hypothesis contradicts the birth year reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
