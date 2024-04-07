# Premise: 10 people voted to watch Skip Beat.
# Hypothesis: more than 10 people voted to watch Skip Beat.
# Golden Label: contradiction

people_voted_premise = 10
people_voted_hypothesis = 10

# the hypothesis refers to the number of people who voted, which is also mentioned in the premise
if people_voted_hypothesis >= people_voted_premise:
    # check if the hypothesis value contradicts the exact number of 'people_voted_premise'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

