# Premise: Morgan Goldman has 5 Senior Managing Directors and 5 Managing Directors.
# Hypothesis: Morgan Goldman has less than 5 Senior Managing Directors and 5 Managing Directors.
# Golden Label: contradiction

senior_managing_directors_premise = 5
managing_directors_premise = 5
senior_managing_directors_hypothesis = 5
managing_directors_hypothesis = 5

# the hypothesis refers to the number of Senior Managing Directors and Managing Directors mentioned in the premise
if senior_managing_directors_hypothesis >= senior_managing_directors_premise:
    # check if the estimate of 'senior_managing_directors_hypothesis' contradicts the number of Senior Managing Directors in the premise
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number of Managing Directors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

