# Premise: Accomplices of the three inmates hijacked a helicopter and forced the pilot to land in the prison courtyard, Interpol said.
# Hypothesis: Three inmates escape from Belgium prison in helicopter.
# Golden Label: neutral

inmates_premise = 3
inmates_hypothesis = 3

# the hypothesis mentions the escape of three inmates from a prison with a helicopter, which is also mentioned in the premise
# however, the hypothesis does not specify the country of the prison, which is mentioned in the premise
# additionally, there is no information in the premise about the inmates escaping, only that a helicopter landed in the courtyard
label = "neutral"

print(label)

