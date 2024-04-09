premise_sentence = "Because even if this sentence is ultimately legal, you may still conclude that it is an immoral one."
hypothesis_sentence = "He says even if the sentence is legal, it may not be a moral one."

# define variables for numerical entities in the premise and hypothesis
volunteers_premise = 0
new_jobs_premise = 0
gdp_growth_premise = 0

# extract numerical entities from the premise and hypothesis
for word in premise_sentence.split():
    if word.isdigit():
        volunteers_premise += int(word)
    elif word == "ultimately":
        new_jobs_premise += int(word)
    elif word == "legal":
        gdp_growth_premise += int(word)

volunteers_hypothesis = 0
new_jobs_hypothesis = 0
gdp_growth_hypothesis = 0

for word in hypothesis_sentence.split():
    if word.isdigit():
        volunteers_hypothesis += int(word)
    elif word == "legal":
        gdp_growth_hypothesis += int(word)

# compare the numerical entities in the premise and hypothesis
if volunteers_hypothesis!= volunteers_premise:
    # check if the number of volunteers in the hypothesis contradicts the number of volunteers in the premise
    label = "contradiction"
elif new_jobs_hypothesis!= new_jobs_premise:
    # check if the number of new jobs from the hypothesis contradicts the number of new jobs in the premise
    label = "contradiction"
elif gdp_growth_hypothesis!= gdp_growth_premise:
    # check if the GDP growth in the hypothesis contradicts the GDP growth reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
