suspects_premise = 4
hostages_premise = "execution"

# define variables for the numerical entities in the premise
suspects_hypothesis = 4

# extract all quantities as valid numbers
suspects_premise = int(suspects_premise)
hostages_premise = hostages_premise.lower()

# compare the variables
if suspects_hypothesis!= suspects_premise:
    # check if the number of suspects in the hypothesis contradicts the number of suspects in the premise
    label = "contradiction"
elif hostages_premise in ["execution", "executions"]:
    # check if the word "execution" or "executions" is present in the hypothesis
    # this is a neutral comparison, as the presence of this word does not entail or contradict the premise
    label = "neutral"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
