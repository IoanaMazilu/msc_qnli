# Premise: What is the height difference between the two if the Empire State Building is more than 135 m tall and the Petronas Towers is 445 m tall?
# Hypothesis: What is the height difference between the two if the Empire State Building is 435 m tall and the Petronas Towers is 445 m tall?
# Golden Label: neutral

ESB_height_premise = 135
ESB_height_hypothesis = 435
PT_height_premise = 445
PT_height_hypothesis = 445

# the hypothesis talks about the height of the Empire State Building and the Petronas Towers mentioned in the premise
if ESB_height_hypothesis <= ESB_height_premise:
    # check if the hypothesis value contradicts the estimate of more than 'ESB_height_premise'
    label = "contradiction"
elif PT_height_hypothesis != PT_height_premise:
    # check if the height of Petronas Towers in the hypothesis contradicts the height of Petronas Towers reported in the premise
    label = "contradiction"
else:
    # the premise gives only an estimate for the height of Empire State Building
    # any height of Empire State Building greater than 'ESB_height_premise' is consistent with the premise, but cannot be explicitly entailed from the premise
    label = "neutral"

print(label)

