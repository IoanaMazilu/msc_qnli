marks_premise = [96, 95, 82, 87, 92]
marks_hypothesis = [<96, 95, 82, 87, 92>]

# the hypothesis talks about the marks obtained by Dacid in different subjects
for subject in marks_hypothesis:
    # check if the hypothesis value for the current subject contradicts the estimate of the premise
    if subject < marks_premise[0]:
        label = "contradiction"
    # if the hypothesis value for the current subject is less than or equal to the premise estimate, we can infer entailment
    elif subject >= marks_premise[0]:
        label = "entailment"
    # if the hypothesis value for the current subject is neutral, we can infer neutrality
    else:
        label = "neutral"

print(label)
