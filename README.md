# e2e_reader
Simple extractor for E2E files to numpy volumes. Scans need to be individually exported as separate E2E files for this to work.
## Requirements
- eyepy
- tqdm

(Run `setup.py` to install all required modules)
```
python setup.py
```

## Usage
Can either extract single E2E file or a folder of multiple E2E files.
```
python extract -i PATH/TO/E2E_FILES_OR_FOLDER -o PATH/TO/OUTPUT_FOLDER
```
