import pytest
import requests

from pubchem import get_compound_info, get_cid_byCAS, get_cid_byname

def test_get_compound_info():
    compound = get_compound_info(2244) #Aspirin's cid number
    assert compound.title == "Aspirin"
    assert compound.molecular_formula == "C9H8O4"
    assert compound.molecular_weight == "180.16"


def test_get_cid_byCAS():
    cid_asprin = get_cid_byCAS("50-78-2") #Aspirin's cas number
    assert cid_asprin == 2244
    cid_gefitnib = get_cid_byCAS("184475-35-2") #Gefitinib's cas number
    assert cid_gefitnib == 123631


def test_get_cid_byname():
    cid_asprin = get_cid_byname("Aspirin") 
    assert cid_asprin == 2244
    cid_gefitnib = get_cid_byname("Gefitinib") 
    assert cid_gefitnib == 123631

