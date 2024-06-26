# define variables for the numerical entities in the premise and hypothesis
potential_jurors_premise = 84
african_americans_premise = 6
potential_jurors_hypothesis = 84
african_americans_hypothesis = 6

# check if the number of African-Americans in the hypothesis contradicts the number of African-Americans in the premise
if african_americans_hypothesis!= african_americans_premise:
    label = "contradiction"
else:
    label = "entailment"

print(label)
