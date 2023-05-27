from versions import (
    python_version,
    requests_version,
    pytest_version
)

# Updated the Python version test to expect the correct version (3.9.x)from 8 to work with my environment instead of 3.8
def test_python_version():
    version_info = python_version()
    assert version_info.major == 3
    # update the version.minor to  9 and not 8
    assert version_info.minor == 9 


def test_requests_version():
    assert requests_version() == "2.27.1"



# Upgrade the pytest version to 7.1.3 using pip
# This will update the pytest version in the virtual environment
# imn the terminal run pip install pytest==7.1.3 to change from my current environment which is 6.2.5
def test_pytest_version():
    assert pytest_version() == "7.1.3"
