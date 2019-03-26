import json
from collections import namedtuple


def parse_arguments(in_hp={}, in_evaluation={}, in_run={}, mode=None):

    with open('parameters/hyperparams.json') as json_file:
        hp = json.load(json_file)
    with open('parameters/evaluation.json') as json_file:
        evaluation = json.load(json_file)
    with open('parameters/run.json') as json_file:
        run = json.load(json_file)
    with open('parameters/environment.json') as json_file:
        env = json.load(json_file)
    with open('parameters/design.json') as json_file:
        design = json.load(json_file)     
        
    #selet the hyperparams for difference mode 
    hp = hp[mode]

    for name,value in in_hp.iteritems():
        hp[name] = value
    for name,value in in_evaluation.iteritems():
        evaluation[name] = value
    for name,value in in_run.iteritems():
        run[name] = value
    
    hp = namedtuple('hp', hp.keys())(**hp)
    evaluation = namedtuple('evaluation', evaluation.keys())(**evaluation)
    run = namedtuple('run', run.keys())(**run)
    env = namedtuple('env', env.keys())(**env)
    design = namedtuple('design', design.keys())(**design)

    return hp, evaluation, run, env, design
