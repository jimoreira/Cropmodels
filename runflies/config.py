# ---------------------------------------------------------------------#
# Configuration file for running the Campbell-Diaz model and optimizer #
#                                                                      #
# Allard de Wit and Deborah Gaso Melgar, Wageningen 2020               #
#----------------------------------------------------------------------#
import sys, os
import yaml

this_dir = os.path.dirname(__file__)
top_dir = os.path.dirname(this_dir)
data_dir = os.path.join(top_dir, "data")

# ------- SETTINGS FOR CAMPBELL-DIAZ MODEL --------

# Weather data
weather_fname = os.path.join(data_dir, "elroble_2000to2024.xlsx")
                             
# model parameters
crop_fname = os.path.join(data_dir, "wofost_soybean_parameters.dat")
soil_fname = os.path.join(data_dir, "soil_parameters.dat")

############# agromanagement South
agromanagement = """
2017:
    campaign_start_date: 2016-11-15
    crop_start_date: 2016-11-15
    crop_end_date: 2017-05-10
2018:
    campaign_start_date: 2017-11-15
    crop_start_date: 2017-11-15
    crop_end_date: 2018-05-10
2019:
    campaign_start_date: 2018-11-15
    crop_start_date: 2018-11-15
    crop_end_date: 2019-05-10
2020:
    campaign_start_date: 2019-11-15
    crop_start_date: 2019-11-15
    crop_end_date: 2020-05-10
2021:
    campaign_start_date: 2020-11-15
    crop_start_date: 2020-11-15
    crop_end_date: 2021-05-10
2022:
    campaign_start_date: 2021-11-15
    crop_start_date: 2021-11-15
    crop_end_date: 2022-05-10
2023:
    campaign_start_date: 2022-11-15
    crop_start_date: 2022-11-15
    crop_end_date: 2023-05-10
2024:
    campaign_start_date: 2023-11-15
    crop_start_date: 2023-11-15
    crop_end_date: 2024-05-10
2025:
    campaign_start_date: 2024-10-15
    crop_start_date: 2024-10-15
    crop_end_date: 2025-05-10
"""
agromanagement = yaml.safe_load(agromanagement)

# --- SETTINGS FOR READING SENTINEL2 DATA ---

farmer='elroble4_ver2324_soja1_clip5.tif'
#farmer='CIRE_mean_Field_mp.tif'
# Dates for Soybean 1ra
#dates = [ '20191122','20191207','20191222', '20200107', '20200122', '20200207', '20200222', '20200307', '20200322', '20200407', '20200422']
#dates = [ '20201122','20201207','20201222', '20210107', '20210122', '20210207', '20210222', '20210307', '20210322', '20210407', '20210422']
dates=['20231027', '20231106',
       '2023116', '20231126',
       '20231206', '20231216',
       '20231226', '20240105',
       '20240115', '20240125',
        '20240204', '20240214',
        '20240224', '20240305',
        '20240315', '20240325',
        '20240404', '20240414',
        '20240424'
       ]

# ['20231027', '20231106',
#        '2023116', '20231126',
#        '20231206', '20231216',
#        '20231226', '20240105',
#        '20240115', '20240125',
#        '20240204', '20240214',
#        '20240224', '20240305',
#        '20240315', '20240325',
#        '20240404', '20240414',
#        '20240424']
# Dates for Soybean 2da
#dates = [ '20191222', '20200107', '20200122', '20200207', '20200222', '20200307', '20200322', '20200407', '20200422', '20200507', '20200522']
#dates = [ '20201222', '20210107', '20210122', '20210207', '20210222', '20210307', '20210322', '20210407', '20210422', '20210507', '20210522']


s2_dir = os.path.join(data_dir, "sentinel2")
polaris_dir = os.path.join(data_dir, "polaris")
# parameters for converting CI to LAI
CI_coefficient = 0.898
CI_offset = 0.904

ensemble_size = 100

# --- SETTINGS FOR THE NLOPT OPTIMIZER ----
parameter_settings = """

FCP:
    default: 0.32
    minimum: 0.23
    maximum: 0.42
    stepsize: 0.03
RDMAX:
    default: 1.
    minimum: 0.4
    maximum: 1.4
    stepsize: 0.05
FNTR:
    default: 3
    minimum: 2
    maximum: 4
    stepsize: 0.1
initLAI:
    default: 0.15
    minimum: 0.08
    maximum: 0.3
    stepsize: 0.01
"""

parameter_settings = yaml.safe_load(parameter_settings)
selected_parameters = ["FCP","RDMAX","FNTR","initLAI"]# 

nlopt_maxeval = 250
nlopt_ftol_rel = 0.001

