"""Tests for the ZALM class functionality."""

import pytest

def test_zalm_run_and_calculate_probability(zalm_instance):
    """Test that ZALM can run and calculate probability of success."""
    # Execute
    import numpy as np
    zalm_instance.params["bsm_efficiency"] = 1 # 0 dB of loss in the BSM
    zalm_instance.params["outcoupling_efficiency"] = 1 # 0 dB of loss in the transmission
    zalm_instance.params["detection_efficiency"] = 1 # So that each mode has equal loss
    zalm_instance.params["mean_photon"] = 10**(-3)
    zalm_instance.run()
    zalm_instance.calculate_probability_success()
    probability = zalm_instance.results['probability_success']

    rhoi = zalm_instance.calculate_density_operator(np.array([1,0,1,1,0,0,1,0]))

    # Assert
    assert probability is not None
    assert rhoi is not None
    assert isinstance(probability, float)
    assert 0 <= probability <= 1, "Probability should be between 0 and 1"