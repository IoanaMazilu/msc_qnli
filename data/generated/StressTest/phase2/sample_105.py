# Premise: Kishore saved 10% of his monthly salary.
# Hypothesis: Kishore saved less than 50% of his monthly salary.
# Golden Label: entailment

saved_percentage_premise = 10
saved_percentage_hypothesis = 50

# the hypothesis refers to the percentage of salary saved by Kishore, mentioned also in the premise
if saved_percentage_hypothesis <= saved_percentage_premise:
    # check if the hypothesis estimate contradicts the premise value of 'saved_percentage_premise'
    label = "contradiction"
elif saved_percentage_premise > saved_percentage_hypothesis:
    # check if the premise value contradicts the hypothesis estimate of less than 'saved_percentage_hypothesis'
    label = "contradiction"
else:
    # if the hypothesis value does not contradict the premise one, we can infer entailment
    label = "entailment"

print(label)

