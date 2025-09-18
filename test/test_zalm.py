"""Tests for the ZALM class functionality."""

import pytest

def test_zalm_run_and_calculate_probability(zalm_instance):
    """Test that ZALM can run and calculate probability of success."""
    # Execute
    zalm_instance.run()
    zalm_instance.calculate_probability_success()
    probability = zalm_instance.results['probability_success']

    # Assert
    assert probability is not None
    assert isinstance(probability, float)
    assert 0 <= probability <= 1, "Probability should be between 0 and 1"