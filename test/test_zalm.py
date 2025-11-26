"""Tests for the ZALM class functionality."""

import numpy as np
import genqo as gq

def test_zalm_run_and_calculate_probability(zalm_instance: gq.ZALM):
    """Test that ZALM can run and calculate probability of success."""
    # Execute
    zalm_instance.params["bsm_efficiency"] = 1 # 0 dB of loss in the BSM
    zalm_instance.params["outcoupling_efficiency"] = 1 # 0 dB of loss in the transmission
    zalm_instance.params["detection_efficiency"] = 1 # So that each mode has equal loss
    zalm_instance.params["mean_photon"] = 1e-3
    zalm_instance.run()

    probability = zalm_instance.calculate_probability_success()
    rhoi = zalm_instance.calculate_density_operator(np.array([1,0,1,1,0,0,1,0]))

    # Assert
    assert probability is not None
    assert rhoi is not None
    assert 0 <= probability <= 1, "Probability should be between 0 and 1"

def test_zalm_run_and_calculate_fidelity(zalm_instance: gq.ZALM):
    """Test that ZALM can run and calculate fidelity."""
    # Execute
    zalm_instance.params["bsm_efficiency"] = 0.9
    zalm_instance.params["outcoupling_efficiency"] = 0.8
    zalm_instance.params["detection_efficiency"] = 0.85
    zalm_instance.params["mean_photon"] = 5e-3
    zalm_instance.run()

    fidelity = zalm_instance.calculate_fidelity()
    rhoi = zalm_instance.calculate_density_operator(np.array([1,0,1,1,0,0,1,0]))

    # Assert
    assert fidelity is not None
    assert rhoi is not None
    assert 0 <= fidelity <= 1, "Fidelity should be between 0 and 1"

def test_hafnian_calculation(zalm_instance: gq.ZALM, benchmark):
    """Benchmark the hafnian calculation in ZALM."""
    # Set up ZALM instance
    zalm_instance.params["bsm_efficiency"] = 0.9
    zalm_instance.params["outcoupling_efficiency"] = 0.8
    zalm_instance.params["detection_efficiency"] = 0.85
    zalm_instance.params["mean_photon"] = 5e-3
    zalm_instance.run()

    # Set up inputs for hafnian calculation
    Cn1 = gq.ZALM.moment_vector([1], 1)
    nA1 = zalm_instance.calculate_k_function_matrix() + zalm_instance.calculate_loss_bsm_matrix_fid()
    basisv = zalm_instance.basisv

    # Benchmark hafnian calculation
    benchmark(gq.tools.W, Cn1, nA1, basisv)
