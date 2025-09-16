# One having run "pip install --upgrade genqo" this script should run without error
import genqo as gq
state_test = gq.ZALM()
state_test.run()
state_test.calculate_probability_success()
state_test.results['probability_success']