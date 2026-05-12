import pandas as pd
from scripts.remove_duplicates import remove_duplicates

def test_remove_duplicates_creates_clean_file(tmp_path):
    # Create a sample dataset with duplicates
    data = pd.DataFrame({
        "id": [1, 1, 2, 3],
        "value": ["A", "A", "B", "C"]
    })
    input_file = tmp_path / "dataset.csv"
    output_file = tmp_path / "dataset_clean.csv"
    data.to_csv(input_file, index=False)

    # Run your function
    remove_duplicates(str(input_file), str(output_file))

    # Read the cleaned file
    cleaned = pd.read_csv(output_file)

    # Assert duplicates are removed
    assert cleaned.shape[0] == 3
    assert 1 in cleaned["id"].values
    assert 2 in cleaned["id"].values
    assert 3 in cleaned["id"].values
