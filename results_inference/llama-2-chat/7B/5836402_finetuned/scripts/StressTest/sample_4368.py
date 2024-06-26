james_worked_premise = 41
james_worked_hypothesis = 51

# the hypothesis refers to the number of hours worked by James, which is also mentioned in the premise
if james_worked_hypothesis >= james_worked_premise:
    # check if the hypothesis value contradicts the estimate of less than 'james_worked_premise'
    label = "contradiction"
elif james_worked_hypothesis < james_worked_premise:
    # check if the hypothesis value is less than the premise value, which implies entailment
    label = "entailment"
else:
    # if the hypothesis value is equal to the premise value, it cannot be explicitly entailed
    label = "neutral"

print(label)
