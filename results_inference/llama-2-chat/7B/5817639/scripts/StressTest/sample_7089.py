salary_premise = 1200
salary_hypothesis = 3200

# the hypothesis talks about Mary's monthly salary, which is also mentioned in the premise
if salary_hypothesis <= salary_premise:
    # check if the hypothesis value contradicts the estimate of Mary's salary in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for Mary's salary, any salary value greater than $1200 is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
