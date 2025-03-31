# Import multiprocessing and set the start method to 'spawn' 
import concurrent.futures

from pysdg.synth.generate import Generator # Import the pysdg Generator
from pysdg.synth.metrics import calc_univar_hellinger_distance # Import a metric function

# A function that will be called by the multiprocessing module. In this function we generate synthetic data and calculate the Hellinger distance between the real and synthetic data.
def my_generator(gen_name, raw_data_path, raw_info_path):
    gen = Generator(gen_name)
    real = gen.load(raw_data_path, raw_info_path)
    gen.train()
    gen.gen(num_rows=len(real), num_synths=1)
    hlngr_dist_data = calc_univar_hellinger_distance(gen.restore_col_names(gen.enc_real), gen.restore_col_names(gen.enc_synths[0]))
    return hlngr_dist_data

if __name__ == "__main__":
    # Define your paths to the raw data and raw info files.
    raw_data_path = 'tutorials/raw_data.csv'
    raw_info_path = 'tutorials/raw_info.json'

    # Define the generator names you want to use.
    gen_names = ['synthcity_bayesian_network', 'synthcity_arf']

    with concurrent.futures.ProcessPoolExecutor(max_workers=2) as executor:
        futures = {executor.submit(my_generator, gen_name, raw_data_path, raw_info_path): gen_name for gen_name in gen_names}
        for future in concurrent.futures.as_completed(futures):
            gen_name = futures[future]
            try:
                result = future.result()
                print(f"Generator: {gen_name}, Hellinger Distance Data Dictionary: {result}")
            except Exception as exc:
                print(f"Generator: {gen_name} generated an exception: {exc}")