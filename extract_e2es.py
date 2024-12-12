import eyepy as ep
import numpy as np
from tqdm import tqdm
import argparse
import os

parser = argparse.ArgumentParser()
parser.add_argument('-i', "--e2e_path", help='folder or file path with E2E files')
parser.add_argument('-o', '--destination_folder', help='folder path where extracted volumes will be kept', default='e2e_volumes')

args = parser.parse_args()
e2e_paths = []
if os.path.isdir(args.e2e_path):
    for file_name in os.listdir(args.e2e_path):
        if file_name.split('.')[-1] == 'E2E':
            e2e_paths.append(os.path.join(args.e2e_path, file_name))
            
elif os.path.isfire(args.e2e_path):
    if args.e2e_path.split('.')[-1] == 'E2E':
        e2e_paths.append(args.e2e_path)

if not os.path.isdir(args.destination_folder):
    os.mkdir(args.destination_folder)

with tqdm(total=len(e2e_paths)) as pbar:
    for idx, e2e_path in enumerate(e2e_paths):
        volume_name = e2e_path.split('/')[-1].split('.')[0]
        pbar.set_description(f'Extracting {volume_name}')
        try:
            ev = ep.import_heyex_e2e(e2e_path)
            np.savez_compressed(os.path.join(args.destination_folder, volume_name), data=ev.data)
        except:
            print(f'Error extracting {volume_name}')
            
        pbar.update(1)