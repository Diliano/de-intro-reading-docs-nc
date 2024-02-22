import pytest


def is_suspicious(crew_mates):
    pass


@pytest.mark.it("Should return False if no imposters are found")
def test_is_not_suspicious():
    assert (
        is_suspicious([])
        is False
    )
    assert (
        is_suspicious(["innocent northcoder"])
        is False
    )
    assert (
        is_suspicious(
            ["renegade northcoder", "imposing northcoder",
             "hard working northcoder"]) is False
    )


@pytest.mark.skip()
@pytest.mark.it("Should return True if an imposter is found")
def test_is_suspicious():
    assert is_suspicious(["imposter"]) is True
    assert is_suspicious(["northcoder happily doing their tasks",
                         "suspicious northcoder", "imposter"]) is True
