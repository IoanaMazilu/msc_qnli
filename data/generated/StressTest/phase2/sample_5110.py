# Premise: Today Roseline, who is less than 60 years old, and her daughter, who is 20 years old, celebrate their birthdays.
# Hypothesis: Today Roseline, who is 50 years old, and her daughter, who is 20 years old, celebrate their birthdays.
# Golden Label: neutral

roseline_age_premise = 60
roseline_age_hypothesis = 50
daughter_age_premise = 20
daughter_age_hypothesis = 20

# the hypothesis refers to the ages of Roseline and her daughter mentioned in the premise
if roseline_age_hypothesis >= roseline_age_premise:
    # check if the age of 'roseline_age_hypothesis' contradicts the estimate of less than 'roseline_age_premise'
    label = "contradiction"
elif daughter_age_hypothesis != daughter_age_premise:
    # check if the age of the daughter in the hypothesis contradicts the age of the daughter reported in the premise
    label = "contradiction"
elif roseline_age_hypothesis == roseline_age_premise - 10:
    # if the age of Roseline in the hypothesis is exactly 10 years less than the upper limit given in the premise, we can infer entailment
    label = "entailment"
else:
    # any age for Roseline less than 'roseline_age_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

