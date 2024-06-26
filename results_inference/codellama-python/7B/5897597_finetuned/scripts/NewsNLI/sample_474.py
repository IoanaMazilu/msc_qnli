matches_premise = 23
relegated_premise = True
impressed_premise = True

impressed_hypothesis = True
relegated_hypothesis = True

# the hypothesis mentions that Varane impressed for Lens despite their relegation from Ligue 1, which is also mentioned in the premise
if impressed_hypothesis!= impressed_premise:
    # check if the impression from the hypothesis contradicts the impression reported in the premise
    label = "contradiction"
elif relegated_hypothesis!= relegated_premise:
    # check if the relegation from the hypothesis contradicts the relegation reported in the premise
    label = "contradiction"
else:
    # if the hypothesis values and estimates do not contradict the premise values, we can infer entailment
    label = "entailment"

print(label)
