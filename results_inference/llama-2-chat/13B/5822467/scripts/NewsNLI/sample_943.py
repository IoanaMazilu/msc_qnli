premise_prohibited_items = ["costumes that cover the face", "containers with more than 1 liter of liquid", "bulky clothes such as vests with pockets"]
hypothesis_deaths = 3
hypothesis_wounded = 260

# define variables with representative names for the numerical entities in both inputs
prohibited_items = set(premise_prohibited_items)
deaths = int(hypothesis_deaths)
wounded = int(hypothesis_wounded)

# extract all quantities as valid numbers (integers or floats)
prohibited_items = [int(item) for item in prohibited_items]
deaths = int(deaths)
wounded = int(wounded)

# compare the variables
if deaths not in prohibited_items:
    # if the number of deaths in the hypothesis does not contradict the prohibited items in the premise, we can infer entailment
    label = "entailment"
elif wounded not in prohibited_items:
    # if the number of wounded in the hypothesis does not contradict the prohibited items in the premise, we can infer entailment
    label = "entailment"
else:
    # if any prohibited item in the hypothesis contradicts the premise, we can infer contradiction
    label = "contradiction"

print(label)
