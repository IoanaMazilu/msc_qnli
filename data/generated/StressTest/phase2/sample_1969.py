# Premise: Morgan Construction has less than 5 Senior Managing Directors and 4 Managing Directors.
# Hypothesis: Morgan Construction has 4 Senior Managing Directors and 4 Managing Directors.
# Golden Label: neutral

senior_managing_directors_premise = 5
senior_managing_directors_hypothesis = 4
managing_directors_premise = 4
managing_directors_hypothesis = 4

# the hypothesis refers to the number of Senior Managing Directors and Managing Directors at Morgan Construction mentioned in the premise
if senior_managing_directors_hypothesis >= senior_managing_directors_premise:
    # check if the number of 'senior_managing_directors_hypothesis' contradicts the number in the premise
    label = "contradiction"
elif managing_directors_hypothesis != managing_directors_premise:
    # check if the number of Managing Directors in the hypothesis contradicts the number reported in the premise
    label = "contradiction"
else:
    # if the hypothesis does not contradict the premise, then it can be inferred as an entailment
    label = "entailment"

print(label)

