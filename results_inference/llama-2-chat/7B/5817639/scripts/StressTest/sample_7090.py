salary_premise = float(input("Premise: "))
salary_hypothesis = float(input("Hypothesis: "))

# compare the hypothesis value to the premise value
if salary_hypothesis <= salary_premise:
    # check if the hypothesis value contradicts the estimate of less than'salary_premise'
    label = "contradiction"
elif salary_hypothesis > salary_premise:
    # the hypothesis value is greater than the premise value, so the hypothesis entails the premise
    label = "entailment"
else:
    # the premise only provides an estimate, so any salary value greater than the estimate is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)
