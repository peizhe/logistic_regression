# -*- coding: utf-8 -*-
import os
import sys
import configure
from lr_train import *

def LoadModel(feature_set):
  f = open(configure.output_model_file_path)
  lines = f.readlines()
  f.close()
  for line in lines:
    tokens = line.strip().split('\t')
    if len(tokens) < 2:
      continue
    feature_set.AddFeature(tokens[0], float(tokens[1]))

if __name__ == '__main__':
  feature_set = FeatureSet()
  LoadModel(feature_set)
  test_case = ["京东","商城","苏宁","易购","国美"]

  feature_list = []
  for feature in test_case:
    if feature in feature_set.features:
      feature_list.append(feature_set.features[feature])
  for feature in feature_list:
    print feature.literal + "\t" + str(feature.weight)
  h = H(feature_list)
  print h
