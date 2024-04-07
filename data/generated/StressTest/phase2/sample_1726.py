# Premise: Apple Infotech has less than 6 Senior Managing Directors and 5 Managing Directors.
# Hypothesis: Apple Infotech has 4 Senior Managing Directors and 5 Managing Directors.
# Golden Label: neutral

senior_directors_premise = 6
senior_directors_hypothesis = 4
managing_directors_premise = 5
managing_directors_hypothesis = 5

# the hypothesis refers to the number of Senior Managing Directors and Managing Directors at Apple Infotech, mentioned in the premise
if senior_directors_hypothesis >= senior_directors_premise:
    # check if the number of Senior Managing Directors in the hypothesis contradicts the estimate of less than 'senior_directors_premise' in the premise
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number of Managing Directors reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"

print(label)

