# Premise: Elsewhere, Mozambique took its first ever Olympic gold medal when Maria Mutola won the women's eight-hundred metres, while the men's ten-thousand-metres went to the Ethiopian Haile Gebrselassie.
# Hypothesis: The women's ten thousand metres champion is from Mozambique.
# Golden Label: neutral

# Representing the races and their winners from the premise and hypothesis
race1_premise = 800
race1_premise_winner = 'Maria Mutola'
race1_premise_country = 'Mozambique'
race2_premise = 10000
race2_premise_winner = 'Haile Gebrselassie'
race2_premise_country = 'Ethiopia'

race_hypothesis = 10000
race_hypothesis_country = 'Mozambique'

# The hypothesis talks about the winner's country of the women's ten-thousand-metre race
# Comparing the race and country of the winner in the hypothesis with the premise
if race_hypothesis == race2_premise and race_hypothesis_country != race2_premise_country:
    # If the race matches but the country doesn't, it is a contradiction
    label = "contradiction"
elif race_hypothesis == race1_premise and race_hypothesis_country != race1_premise_country:
    # If the race matches but the country doesn't, it is a contradiction
    label = "contradiction"
else:
    # If the country of the winner in the hypothesis does not match any of the countries in the premise,
    # it cannot be entailed nor contradicted, so it is neutral
    label = "neutral"

print(label)

