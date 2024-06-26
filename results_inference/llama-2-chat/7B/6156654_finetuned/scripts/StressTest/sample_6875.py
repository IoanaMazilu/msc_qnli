days_worked_premise = 60
days_worked_hypothesis = 60

# the hypothesis talks about the number of days worked by Jhon, which is also mentioned in the premise
if days_worked_hypothesis >= days_worked_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
elif days_worked_hypothesis < days_worked_premise:
    # check if the hypothesis value is less than the premise value, which is neutral
    label = "neutral"
else:
    # if the hypothesis value is equal to the premise value, it is not contradictory or neutral
    label = "entailment"

print(label)
