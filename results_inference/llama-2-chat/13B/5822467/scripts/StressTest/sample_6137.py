james_hours_premise = 41
james_hours_hypothesis = float(input("Enter the number of hours James worked last week: "))
harry_hours_hypothesis = float(input("Enter the number of hours Harry worked last week: "))

# the hypothesis refers to the number of hours James and Harry worked
if james_hours_premise <= james_hours_hypothesis:
    # check if the estimate of 'james_hours_hypothesis' contradicts the number of hours James worked in the premise
    label = "contradiction"
elif harry_hours_hypothesis!= james_hours_premise:
    # check if the number of hours Harry worked in the hypothesis contradicts the number of hours James worked in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)
