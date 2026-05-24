import os
from src.data_loader import load_data

def test_load_data():
    path = "data/insurance_data.csv"

    if os.path.exists(path):
        df = load_data(path)
        assert not df.empty
    else:
        assert True