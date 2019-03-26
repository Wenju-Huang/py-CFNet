# py-CFNet
Python (Tensorflow) implementation of [CFNet tracker](http://www.robots.ox.ac.uk/~luca/cfnet.html)

## Settings things up with virtualenv
1) Get virtualenv if you don't have it already
`pip install virtualenv`
1) Create new virtualenv with Python 2.7
`virtualenv --python=/usr/bin/python2.7 ve-tracking`
1) Activate the virtualenv
`source ~/ve-tracking/bin/activate`
1) Clone the repository
`https://github.com/Wenju-Huang/py-CFNet.git`
1) `cd py-CFNet`
1) Install the required packages
`sudo pip install -r requirements.txt`
1) `mkdir pretrained data`
1) Download the [pretrained networks](https://bit.ly/cfnet_networks) in `pretrained` and unzip the archive 



## Running the tracker
1) Set `root_dataset` in `parameters/environment.json` to the root path of your evaluation dataset (don't include the dataset name)
1) Set `dataset` in `parameters/evaluation.json` to the name your evaluation dataset (e.g. `"CVPR2013"`)
1) Set `video` in `parameters/evaluation.json` to `"all"` or to a specific sequence (e.g. `"vot2016_ball1"`)
1) See if you are happy with the default parameters in `parameters/hyperparameters.json`
1) Select the model you want to run at line 18 in `python run_tracker_evaluation.py` (default is `'conv2'`)
1) Call the main script (within an active virtualenv session)
`python run_tracker_evaluation.py`

## Results
OTB2013 -- Precision (20 px): 73.83 --  Success AUC: 0.55 -- FPS: 42.97 FPS
## Acknowledgments
Many parts of this code are adopted from the related works [siamfc-tf](https://github.com/torrvision/siamfc-tf)

