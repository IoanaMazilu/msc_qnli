scientific_question_premise = 7
scientific_question_hypothesis = 7

# the hypothesis refers to the time required for a train to cover the distance between Chennai and Jammu, mentioned in the premise
if scientific_question_hypothesis <= scientific_question_premise:
    # check if the hypothesis value contradicts the premise value
    label = "entailment"
elif scientific_question_hypothesis > scientific_question_premise + 1:
    # check if the hypothesis value contradicts the premise value
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise value, we can infer neutral
    label = "neutral"

print(label)
