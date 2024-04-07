# Premise: Another survey of less than 520 people in the town of Angie found that 60% preferred Brand A.
# Hypothesis: Another survey of 120 people in the town of Angie found that 60% preferred Brand A.
# Golden Label: neutral

survey_people_premise = 520
survey_people_hypothesis = 120

# The hypothesis is referring to the number of surveyed people in the town of Angie mentioned in the premise
if survey_people_hypothesis >= survey_people_premise:
    # Check if the number of surveyed people in the hypothesis contradicts the estimate of less than 'survey_people_premise'
    label = "contradiction"
elif survey_people_hypothesis < survey_people_premise and survey_people_hypothesis > 0:
    # The premise only provides an upper limit for the number of surveyed people
    # Any number of surveyed people less than 'survey_people_premise' is consistent with the premise, but cannot be explicitly entailed from it
    label = "neutral"
else:
    label = "contradiction"

print(label)

