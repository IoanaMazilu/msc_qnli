# define variables for the numerical entities in the premise and hypothesis
rape_premise = 17
survey_hypothesis = 17

# check if the number of girls under 17 in the hypothesis contradicts the number of girls under 17 in the premise
if survey_hypothesis!= rape_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
