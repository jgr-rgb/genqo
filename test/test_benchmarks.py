"""Benchmarks for genqo package."""

import genqo as gq


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
    