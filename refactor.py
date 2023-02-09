'''
Jonathan Sosa
refactor.py
Feb 2023
'''

#imports
import emip_toolkit as EMTK
import correction
import numpy as np
import drift_algorithms as algo
from tqdm import tqdm

#functions
def attachCorrection(data, line_ys, aoi, robot_index):
    '''
    corrects the data with the noise and corrects the data

    Parameters
    ------------------------------
    data: data with the error
    line_ys: y = y coordinates for each line
    aoi: areas of interest
    robot_index: gets the index of the robot we are testing the data on
    '''

    np_array = np.array(data.copy())
    attach_correction = algo.attach(np_array, line_ys)
    percentage, match_list = correction.correction_quality(aoi, data['robot' + str(robot_index)].copy(), attach_correction)
    return percentage

