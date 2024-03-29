from datetime import date
from io import StringIO
from elections import Election, Jurisdiction

# A string representing one election result.
# StringIO will take the string below and make an object that we can pass to
# method read_results just like we would pass an open file to it.
# We use this in our testing below. You can use it in your own testing, but
# you do not have to.
SHORT_FILE_CONTENTS = 'header\n' + \
                      ','.join(['35090', '"St. Paul\'s"', '"St. Paul\'s"',
                                '" 1"', '"Toronto"', 'N', 'N', '""', '1',
                                '367', '"Bennett"', '""', '"Carolyn"',
                                '"Liberal"', '"Liberal"', 'Y', 'Y', '113'])


def simple_election_setup() -> Election:
    """Set up a simple Election with two ridings and three parties"""
    e = Election(date(2000, 2, 8))
    e.update_results('r1', 'ndp', 1234)
    e.update_results('r1', 'lib', 1345)
    e.update_results('r1', 'pc', 1456)

    e.update_results('r2', 'ndp', 300)
    e.update_results('r2', 'lib', 200)
    e.update_results('r2', 'pc', 100)

    return e


def simple_jurisdiction_setup() -> Jurisdiction:
    """Set up a simple Jurisdiction with a single Election and one result."""
    j = Jurisdiction('Canada')
    res1 = StringIO(SHORT_FILE_CONTENTS)
    j.read_results(2000, 1, 2, res1)
    return j


def test_simple_election_ridings_recorded() -> None:
    """Test Election.ridings_recorded with a simple Election."""
    e = simple_election_setup()
    assert e.ridings_recorded() == ['r1', 'r2']


def test_simple_election_results_for() -> None:
    """Test Election.results_for with a simple Election."""
    e = simple_election_setup()
    assert e.results_for('r1', 'ndp') == 1234


def test_simple_election_riding_winners() -> None:
    """Test Election.riding_winners with a simple Election."""
    e = simple_election_setup()
    assert e.riding_winners('r1') == ['pc']


def test_simple_election_popular_vote() -> None:
    """Test Election.popular_vote with a simple Election."""
    e = simple_election_setup()
    assert e.popular_vote() == {'ndp': 1534, 'lib': 1545, 'pc': 1556}


def test_simple_election_party_seats() -> None:
    """Test Election.party_seats with a simple Election."""
    e = simple_election_setup()
    assert e.party_seats() == {'ndp': 1, 'lib': 0, 'pc': 1}


def test_one_party_one_riding_read_results() -> None:
    """Test Election.read_results with a file with a single line."""
    file = StringIO(SHORT_FILE_CONTENTS)
    e = Election(date(2012, 10, 30))
    e.read_results(file)
    assert e.popular_vote() == {'Liberal': 113}


def test_simple_jurisdiction_party_wins() -> None:
    """Test Jurisdiction.party_wins with a file with a single line. """
    j = simple_jurisdiction_setup()
    assert j.party_wins('Liberal') == [date(2000, 1, 2)]


def test_simple_jurisdiction_party_history() -> None:
    """Test Jurisdiction.party_history with a file with a single line."""
    j = simple_jurisdiction_setup()
    assert j.party_history('Liberal') == {date(2000, 1, 2): 1.0}


def test_simple_jurisdiction_riding_changes() -> None:
    """Test Jurisdiction.riding_changes with two Elections."""
    j = simple_jurisdiction_setup()
    res2 = open('data/toronto-stpauls.csv')
    j.read_results(2004, 5, 15, res2)
    res2.close()
    assert j.riding_changes() == [({"St. Paul's"}, {"Toronto--St. Paul's"})]


if __name__ == '__main__':
    import pytest
    pytest.main(['a0_sample_test.py'])
