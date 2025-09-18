"""Pytest configuration for genqo tests."""

import pytest

# Add any shared fixtures here
@pytest.fixture
def zalm_instance():
    """Return a basic ZALM instance for testing."""
    import genqo as gq
    return gq.ZALM()