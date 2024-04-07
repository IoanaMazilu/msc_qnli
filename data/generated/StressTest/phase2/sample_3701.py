# Premise: Today Katherine, who is 40 years old, and her daughter, who is 10 years old, celebrate their birthdays.
# Hypothesis: Today Katherine, who is more than 40 years old, and her daughter, who is 10 years old, celebrate their birthdays.
# Golden Label: contradiction

katherine_age_premise = 40
katherine_age_hypothesis = 40
daughter_age_premise = 10
daughter_age_hypothesis = 10

# the hypothesis mentions the same ages for Katherine and her daughter as in the premise
if katherine_age_hypothesis != katherine_age_premise:
    # check if the age of Katherine in the hypothesis contradicts the age of Katherine in the premise
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of the daughter in the hypothesis contradicts the age of the daughter in the premise
    label = "contradiction"
else:
    # if the ages in the hypothesis do not contradict the ones in the premise, we can infer entailment
    label = "entailment"

print(label)

