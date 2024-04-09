% import logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)

def compare_entities(premise, hypothesis):
    # Define variables for the numerical entities in the premise and hypothesis
    premise_entities = {
        'people_dead_by_bombardment': float(premise['people_dead_by_bombardment']),
       'remainder_left_village_on_fear': float(premise['remainder_left_village_on_fear'])
    }
    hypothesis_entities = {
        'people_dead_by_bombardment': float(hypothesis['people_dead_by_bombardment']),
       'remainder_left_village_on_fear': float(hypothesis['remainder_left_village_on_fear'])
    }

    # Extract all quantities as valid numbers
    premise_quantities = [
        float(x) for x in premise_entities.keys()
    ]
    hypothesis_quantities = [
        float(x) for x in hypothesis_entities.keys()
    ]

    # Compare the quantities between the premise and hypothesis
    # Use brief comments to explain the comparison
    # Do not use their values in the comments
    for quantity in premise_quantities:
        if quantity > hypothesis_quantities[0]:
            logging.info('entailment: more than %s people died by bombardment in the hypothesis', quantity)
        elif quantity < hypothesis_quantities[0]:
            logging.info('contradiction: less than %s people died by bombardment in the premise', quantity)
        else:
            logging.info('neutral: the number of people who died by bombardment in the hypothesis is consistent with the premise')

    for quantity in hypothesis_quantities:
        if quantity > premise_quantities[0]:
            logging.info('entailment: more than %s people left the village on account of fear in the hypothesis', quantity)
        elif quantity < premise_quantities[0]:
            logging.info('contradiction: less than %s people left the village on account of fear in the premise', quantity)
        else:
            logging.info('neutral: the number of people who left the village on account of fear in the hypothesis is consistent with the premise')

# Return the label indicating the relation between the premise and hypothesis
return 'entailment' if any('entailment') else 'neutral'
