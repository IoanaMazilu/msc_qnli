# Premise: TJ Jackson, 34, is the son of Tito Jackson and the late Delores Martes Jackson.
# Hypothesis: T.J. Jackson and his two brothers are the sons of Tito Jackson.
# Golden Label: neutral

age_premise = 34
sons_hypothesis = 3

# the hypothesis mentions TJ Jackson and his two brothers as sons of Tito Jackson, while the premise only confirms TJ Jackson as Tito Jackson's son
# the premise does not provide information about TJ Jackson's siblings, so we cannot confirm or contradict the number of brothers as per the hypothesis
label = "neutral"

print(label)

