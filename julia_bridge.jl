using PythonCall
using CondaPkg

# Ensure CondaPkg is resolved
CondaPkg.resolve()

# Install pip and genqo in the conda environment
CondaPkg.add("pip")
CondaPkg.resolve()

# Now import Python modules
py_sys = pyimport("sys")
py_subprocess = pyimport("subprocess")
println("Using Python from: ", py_sys.executable)

# Install genqo using pip
py_subprocess.check_call([py_sys.executable, "-m", "pip", "install", "genqo"])

# Use genqo
gq = pyimport("genqo")
state = gq.ZALM()
state.run()
state.calculate_probability_success()
probability = state.results["probability_success"]
println("Probability of success: ", probability)