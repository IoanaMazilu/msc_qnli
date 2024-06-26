chiefs_of_staff_premise = 3
chiefs_of_staff_hypothesis = 5

# the hypothesis refers to the number of Joint Chiefs of Staff mentioned in the premise
if chiefs_of_staff_premise >= chiefs_of_staff_hypothesis:
    # check if the premise number contradicts the hypothesis estimate of less than 'chiefs_of_staff_hypothesis'
    label = "contradiction"
else:
    # if the premise number does not contradict the hypothesis estimate, we infer entailment
    label = "entailment"

print(label)
