# The premise and hypothesis have different conditions for the number of hours worked
# The premise states 'the first 40 hours' and 'less than 60 hours'
# The hypothesis states 'the first 60 hours'

hours_worked_premise = 40
hours_worked_hypothesis = 60

if hours_worked_premise >= hours_worked_hypothesis:
    # check if the number of hours in the premise contradicts the number of hours in the hypothesis
    label = "contradiction"
elif hours_worked_premise < hours_worked_hypothesis:
    # check if the number of hours in the premise entails the number of hours in the hypothesis
    label = "entailment"
else:
    # if the number of hours in the premise and the hypothesis are the same, the relation is neutral
    label = "neutral"

print(label)
