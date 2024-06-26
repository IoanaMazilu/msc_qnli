premise = "During the first two weeks of March, the total rainfall in Springdale was 25 inches."
hypothesis = "During the first two weeks of March, the total rainfall in Springdale was more than 25 inches."

# extract the numerical entities from the premise and hypothesis
premise_rainfall = 25
hypothesis_rainfall = 25

# check if the hypothesis value contradicts the premise value
if hypothesis_rainfall <= premise_rainfall:
    label = "contradiction"
else:
    label = "entailment"

print(label)
