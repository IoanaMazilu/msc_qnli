# Premise: Today Katherine, who is less than 70 years old, and her daughter, who is 10 years old, celebrate their birthdays.
# Hypothesis: Today Katherine, who is 40 years old, and her daughter, who is 10 years old, celebrate their birthdays.
# Golden Label: neutral

katherine_age_premise = 70
katherine_age_hypothesis = 40
daughter_age_premise = 10
daughter_age_hypothesis = 10

# the hypothesis refers to the age of Katherine and her daughter mentioned in the premise
if katherine_age_hypothesis >= katherine_age_premise:
    # check if the age of Katherine in the hypothesis contradicts the age mentioned in the premise
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of the daughter in the hypothesis contradicts the age reported in the premise
    label = "contradiction"
elif katherine_age_hypothesis <= katherine_age_premise and daughter_age_hypothesis == daughter_age_premise:
    # if the hypothesis values and estimates do not contradict the premise ones, we can infer entailment
    label = "entailment"
else:
    # the premise gives only an estimate for the age of Katherine
    # any age less than 'katherine_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

