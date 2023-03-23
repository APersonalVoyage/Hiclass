import sys,os,pdb
import numpy as np
from scipy import interpolate, integrate
from cosmosis.datablock import names, option_section

likes = names.likelihoods
options = option_section
cosmo = names.cosmological_parameters
distances = names.distances

run_dir=os.path.split(__file__)[0] #detect path of this directory

def setup(block):
    datadir = block.get_string(options,"dirname", default=run_dir)
    datafile = block.get_string(options, "filename")
    datapath = os.path.join(datadir,datafile)

    d_gw_obs, z_obs, sigma_dgw, sigma_z, v_rms = np.loadtxt(datapath, unpack=True, comments='#')


    return d_gw_obs, z_obs, sigma_dgw, sigma_z, v_rms

def likelihood(data_vec, block):

    #Get dl(z) for theory model
    z_model_table = block[distances, 'z']
    dl_model_table = block[distances, 'd_l']
    h_model_table = block[distances, 'h']
    dgw_ratio_model_table = block[distances, 'd_l_gw_on_d_l_em']

    #Make sure z is increasing
    if z_model_table[1]<z_model_table[0]:
        z_model_table = z_model_table[::-1]
        dl_model_table = dl_model_table[::-1]
    
    dgw_model_table = dgw_ratio_model_table*dl_model_table
    
    d_gw_obs, z_obs, sigma_dgw, sigma_z, v_rms = data_vec

    # get cosomological parameters for H(z)
    Hz_spl = interpolate.UnivariateSpline(z_model_table, 3.e5*h_model_table, k=1, s=0)
    Hz = Hz_spl(z_obs)

    dl_spl = interpolate.UnivariateSpline(z_model_table, dl_model_table, k=1, s=0)
    dl_dspl = dl_spl.derivative()
    d_theory = dl_spl(z_obs)
    dd_gwdz = dl_dspl(z_obs)

    dgw_spl = interpolate.UnivariateSpline(z_model_table, dgw_model_table, k=1, s=0)
    dgw_dspl = dgw_spl.derivative()
    d_gw_theory = dgw_spl(z_obs)


    sigma_n = np.sqrt(sigma_dgw**2. + (dd_gwdz*sigma_z)**2.)
    sigma_lens = d_gw_obs*0.066*((1. - (1 + z_obs)**-0.25)/0.25)**1.8 # Tamanini et al eq.7.3
    sigma_v = d_gw_obs*(1 + 3.e5*(1. + z_obs)/(Hz*d_gw_obs))*(v_rms/3.e5)
    
    chisquare = (1./(sigma_n**2. + sigma_lens**2. + sigma_v**2.))*(d_gw_obs - d_gw_theory)**2.
    LogLike = -0.5*chisquare.sum()
    return LogLike
  
def execute(block,config):

    #calculate the log-likelihood
    LogLike=likelihood(config, block)

    #Give a little warning about infinity and NaN errors
    if not np.isfinite(LogLike):
        sys.stderr.write("Non-finite LogLike in d_gw_like\n")

    #Save the result
    block[likes, 'DGW_LIKE'] = float(LogLike)

    #Signal success
    return 0
