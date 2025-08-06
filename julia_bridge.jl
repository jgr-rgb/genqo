using CondaPkg
CondaPkg.add("genqo")
using PythonCall
gq = pyimport("genqo")
state = gq.ZALM()
state.run()
state.calculate_probability_success()
