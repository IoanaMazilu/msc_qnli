salary_saved_premise = 10
salary_saved_hypothesis = 80

# the hypothesis refers to the percentage of salary saved by Kishore, which is also mentioned in the premise
if salary_saved_hypothesis <= salary_saved_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
elif salary_saved_premise >= salary_saved_hypothesis:
    # check if the premise value contradicts the hypothesis
    label = "contradiction"
else:
    # any saving percentage less than 'salary_saved_hypothesis' is consistent with the premise
    # but since the premise does not specify an upper limit, we cannot explicitly entail the hypothesis from the premise
    label = "neutral"

print(label)
