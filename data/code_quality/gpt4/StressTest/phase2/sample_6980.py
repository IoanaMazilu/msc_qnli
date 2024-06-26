directors_premise = 8
directors_hypothesis = 8

# the hypothesis refers to the number of persons serving on the board of each charity mentioned in the premise
if directors_hypothesis >= directors_premise:
    # check if the hypothesis value contradicts the exact number of 'directors_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)
