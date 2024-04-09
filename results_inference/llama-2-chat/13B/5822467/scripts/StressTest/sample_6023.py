borrowed_premise = 5000
borrowed_hypothesis = 3000

# the hypothesis refers to the amount of money borrowed for college education
if borrowed_hypothesis <= borrowed_premise:
    # check if the hypothesis value contradicts the estimate of 'borrowed_premise'
    label = "contradiction"
elif borrowed_hypothesis!= borrowed_premise:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value and estimate do not contradict the premise value, we can infer entailment
    label = "entailment"

print(label)
