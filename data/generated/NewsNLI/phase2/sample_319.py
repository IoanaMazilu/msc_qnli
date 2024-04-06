# Premise: Since receiving the biggest bail out in history, RBS has announced 27,500 layoffs worldwide -- of which 21,200 are in the UK.
# Hypothesis: RBS has announced 27,500 layoffs worldwidel ; 21,200 alone in the UK.
# Golden Label: entailment

layoffs_worldwide_premise = 27500
layoffs_UK_premise = 21200
layoffs_worldwide_hypothesis = 27500
layoffs_UK_hypothesis = 21200

# the hypothesis mentions the total worldwide layoffs and the UK layoffs, which are also mentioned in the premise
if layoffs_worldwide_hypothesis != layoffs_worldwide_premise:
    # check if the total worldwide layoffs in the hypothesis contradicts the total worldwide layoffs reported in the premise
    label = "contradiction"
elif layoffs_UK_hypothesis != layoffs_UK_premise:
    # check if the UK layoffs from the hypothesis contradicts the UK layoffs in the premise
    label = "contradiction"
else:
    # if the hypothesis values do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)

