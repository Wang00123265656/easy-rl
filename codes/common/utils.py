#!/usr/bin/env python
# coding=utf-8
'''
Author: John
Email: johnjim0816@gmail.com
Date: 2021-03-12 16:02:24
LastEditor: John
LastEditTime: 2021-04-03 21:42:13
Discription: 
Environment: 
'''
import os
import numpy as np


def save_results(rewards,ma_rewards,tag='train',path='./results'):
    '''保存reward等结果
    '''
    np.save(path+'rewards_'+tag+'.npy', rewards)
    np.save(path+'ma_rewards_'+tag+'.npy', ma_rewards)
    print('results saved!')

def make_dir(*paths):
    for path in paths:
        if not os.path.exists(path): # check if exists
            os.mkdir(path)
def del_empty_dir(*paths):
    '''del_empty_dir delete empty folders unders "paths"
    '''
    for path in paths:
        dirs = os.listdir(path)
        for dir in dirs:
            if not os.listdir(os.path.join(path, dir)):
                os.removedirs(os.path.join(path, dir))