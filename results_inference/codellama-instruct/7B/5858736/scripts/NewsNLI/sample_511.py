# Define variables for the premise and hypothesis
suarez_experience = 0
cano_experience = 0
suarez_time_served = 0
cano_time_served = 0

# Extract numerical information from the premise
suarez_experience = int(re.search(r"(\d+) military experience", premise).group(1))
cano_experience = int(re.search(r"(\d+) military experience", premise).group(1))
suarez_time_served = int(re.search(r"(\d+) time served in the FARC", premise).group(1))
cano_time_served = int(re.search(r"(\d+) time served in the FARC", premise).group(1))

# Check if the hypothesis is entailed from the premise
if suarez_experience > cano_experience:
    label = "entailment"
elif suarez_time_served > cano_time_served:
    label = "entailment"
else:
    label = "neutral"

print(label)
