import pytest
from dags.src.data.pre_process import conver_to_list, process_list
from unittest.mock import patch, Mock
from pathlib import Path
import pandas as pd

# Test for conver_to_list function
def test_conver_to_list(tmpdir):
    # Mocking pandas read_csv function and to_csv method
    mock_read_csv = Mock(return_value=pd.DataFrame({'tokens': ['["token1", "token2"]', '["token3", "token4"]']}))
    mock_to_csv = Mock()
    mock_logger = Mock()

    with patch('pandas.read_csv', mock_read_csv), \
         patch('pandas.DataFrame.to_csv', mock_to_csv):
        project_folder = Path(tmpdir)
        file_name = "test"

        result = conver_to_list(project_folder, file_name, mock_logger)

        # Check if the function returned None (indicating success)
        assert result is None

        # Check if to_csv is called to write processed data
        assert mock_to_csv.called

# Test for process_list function
def test_process_list():
    input_list = ["123", "Token"]
    expected_output = ["[num]", "token"]
    assert process_list(input_list) == expected_output
