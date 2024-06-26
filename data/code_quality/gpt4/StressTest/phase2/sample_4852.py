salary_percent_saved_premise = 70
salary_percent_saved_hypothesis = 10

# the hypothesis talks about the percent of Kishore's salary that he saved, which is also referenced in the premise
if salary_percent_saved_hypothesis >= salary_percent_saved_premise:
    # check if the hypothesis value contradicts the estimation of less than 'salary_percent_saved_premise'
    label = "contradiction"
else:
    # the premise gives an estimate for the maximum percentage of salary saved
    # any percentage less than 'salary_percent_saved_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
