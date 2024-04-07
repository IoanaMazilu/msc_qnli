# Premise: In a shop, 40% socks are white and rest are black.
# Hypothesis: In a shop, more than 40% socks are white and rest are black.
# Golden Label: contradiction

white_socks_percentage_premise = 40
white_socks_percentage_hypothesis = 40

# the hypothesis talks about the percentage of white socks in a shop, also mentioned in the premise
if white_socks_percentage_hypothesis <= white_socks_percentage_premise:
    # check if the hypothesis value contradicts the value of 'white_socks_percentage_premise'
    label = "contradiction"
else:
    # the premise gives a specific percentage for the white socks
    # any percentage greater than 'white_socks_percentage_premise' contradicts the premise
    label = "contradiction"

print(label)

