import kagglehub

def download_kaggle_dataset(dataset_name: str) -> str:
    """
    Downloads a dataset from Kaggle using the kagglehub library.
    
    Args:
        dataset_name (str): The Kaggle dataset identifier 
                            (e.g., 'mssmartypants/rice-type-classification').
                            
    Returns:
        str: The local path to the downloaded dataset files.
    """
    print(f"Downloading dataset '{dataset_name}' using kagglehub...")
    path = kagglehub.dataset_download(dataset_name)
    print(f"✅ Dataset available at: {path}")
    return path
