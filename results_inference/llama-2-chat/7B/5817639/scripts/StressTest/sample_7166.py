people_entered_premise = 15
people_entered_hypothesis = float("+inf")  # infinity represents "more than"

# the hypothesis talks about the number of people entered a theater before Sujit, while the premise gives a fixed number
if people_entered_hypothesis <= people_entered_premise:
    # check if the hypothesis value contradicts the estimate of 'people_entered_premise'
    label = "contradiction"
else:
    # the premise gives a fixed number, while the hypothesis refers to a greater number, so we can infer entailment
    label = "entailment"

print(label)
