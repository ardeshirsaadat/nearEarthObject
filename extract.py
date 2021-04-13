"""Extract data on near-Earth objects and close approaches from CSV and JSON files.

The `load_neos` function extracts NEO data from a CSV file, formatted as
described in the project instructions, into a collection of `NearEarthObject`s.

The `load_approaches` function extracts close approach data from a JSON file,
formatted as described in the project instructions, into a collection of
`CloseApproach` objects.

The main module calls these functions with the arguments provided at the command
line, and uses the resulting collections to build an `NEODatabase`.

You'll edit this file in Task 2.
"""
import csv
import json

from models import NearEarthObject, CloseApproach


def load_neos(neo_csv_path):
    """Read near-Earth object information from a CSV file.

    :param neo_csv_path: A path to a CSV file containing data about near-Earth objects.
    :return: A collection of `NearEarthObject`s.
    """
    collections = []
    # TODO: Load NEO data from the given CSV file.
    with open(neo_csv_path, 'r') as readfile:
        read = csv.DictReader(readfile)
        for row in read:
            collections.append(NearEarthObject(
                pdes=row['pdes'], name=row['name'], diameter=row['diameter'], pha=row['pha']))

    return collections


def load_approaches(cad_json_path):
    """Read close approach data from a JSON file.

    :param neo_csv_path: A path to a JSON file containing data about close approaches.
    :return: A collection of `CloseApproach`es.
    """
    # TODO: Load close approach data from the given JSON file.
    collections = []
    with open(cad_json_path) as readfile:
        read = json.load(readfile)
    for data in read['data']:
        collections.append(CloseApproach(
            des=data[0], cd=data[3], dist=data[4], v_rel=data[7]))
    return collections
