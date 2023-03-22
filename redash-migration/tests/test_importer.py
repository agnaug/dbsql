from __future__ import annotations


def test_import_query():
    # Our Libraries
    from redash_migration.importer import import_query

    given = 1
    output = import_query(given)
    expected = {}

    assert output == expected
