# dirty-dish-neural-network
## Author: Cristian Madrazo

A machine learning project that classifies images of dishes as either dirty or clean using a convolutional neural 
network coupled with SIFT (Scale-Invariant Feature Transform). This project demonstrates the use of deep learning and 
feature extraction techniques for binary classification.

## References
SIFT Functions from OpenCV: https://docs.opencv.org/4.x/da/df5/tutorial_py_sift_intro.html

SIFT-CNN Research Paper by Dimitrios Tsourounis: https://www.mdpi.com/2313-433X/8/10/256

Idea and Dataset (modified in this project) from Igor Slinko on Kaggle: https://www.kaggle.com/competitions/platesv2

Wikipedia CNN: https://en.wikipedia.org/wiki/Convolutional_neural_network

IBM CNN: https://www.ibm.com/topics/convolutional-neural-networks

## Python Virtual Environment Setup
Make sure you have python 3.10 installed on your machine
Make sure you are in the project root directory `dirty-dish-neural-network/`
To setup the environment first create a virtual environment: `python3.10 -m venv .venv`
Then activate the environment: `source .venv/vin/activate`
Then install the dependencies: `pip install -r requirements.txt`


## Notebook Environment Setup
Follow these instructions if you will also be running the notebooks
First follow all instructions to setup the python virtual environment
Then run the kernel setup script:  `./create_venv_kernel.sh`
Now select .venv as your Jupyter kernel and run the cells
Note that you may need to restart your IDE to see updated kernels

## How to Run Notebooks
The notebooks are used to process the training data and train the model
Running the notebooks can be difficult because of access to the training data
If you cloned from git, then you won't have my training data due to the size. 
Start at step 1.

If you obtained a zip file from me, then you will have everything you need to run the notebooks. 
Start at step 2.

1. Populate `src/data/train/clean/`with images of clean plates and `src/data/train/dirty/` with images of dirty plates.
2. Follow all the instructions above to set up and activate a python virtual environment
3. Follow all the instructions above to set up the notebook environment
4. Click Run All Cells in the `src/process_data.ipynb` notebook
4. Click Run All Cells in the `src/train_model.ipynb` notebook

## How to Run/Test the User Interface
The saved model is not ignored in this repo so my last run of  `src/train_model.ipynb` 
saves `src/data/models/cnn_model.keras` which is committed to the repo.
Therefore user interface program can be run out of the box regardless of where you obtained this source code

1. Follow all the instructions above to set up and activate a python virtual environment
2. From the project root, run `python src/app.py`
3. Enter http://127.0.0.1:5000 into your web browser
4. Try submitting any of the images in `src/data/testing/`
5. The classification should appear immediately on your screen, check the terminal for logging or errors

## Additional Documentation
If you are curious as to the why or how for anything in this project, your question might be answered by 
the supplemental documentation in `documents/`
Notably, there are demo videos there, flowcharts, and reports
