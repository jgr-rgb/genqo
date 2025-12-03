# Create a virtual environment and install genqo
venv:
    python -m venv .venv
    . .venv/bin/activate && just install

# Install genqo in editable mode
install:
    pip install -e .[test]

# Run test suite
test:
    pytest test/test_zalm.py

# Run benchmarks only
alias bm := benchmark
benchmark:
    pytest test/test_benchmarks.py
    