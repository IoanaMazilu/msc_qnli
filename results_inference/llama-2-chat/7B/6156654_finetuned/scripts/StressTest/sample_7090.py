salary_mary_premise = 3200
salary_mary_hypothesis = 1200

# the hypothesis talks about Mary's salary, which is also mentioned in the premise
if salary_mary_hypothesis >= salary_mary_premise:
    # check if the hypothesis value contradicts the premise
    label = "contradiction"
else:
    # if the hypothesis value is less than the premise value, we can infer entailment
    label = "entailment"

print(label)
