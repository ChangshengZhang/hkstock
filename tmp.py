#!/usr/bin/python
# -*- coding: utf-8 -*-
# File Name: tmp.py
# Author: Changsheng Zhang
# mail: zhangcsxx@gmail.com
# Created Time: Wed Oct 18 22:54:17 2017

#########################################################################

import os,sys,glob
from git import *

repo=Repo('.')
index=repo.index
index.add(repo.untracked_files)
newcommit=index.commit('Regular')
origin=repo.remotes.origin
origin.push()
