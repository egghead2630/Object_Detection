# VRDL_HW2
-------------------------------------------------------------------------
This repository is the official implementation of My VRDL_HW2: Object detection



Requirements
-------------------------------------------------------------------------
Python version:
	
	Python 3.9.7

pytorch:
	
	pip3 install torch==1.10.0+cu113 torchvision==0.11.1+cu113 torchaudio===0.10.0+cu113 -f https://download.pytorch.org/whl/cu113/torch_stable.html

yolov5:
	
	git clone https://github.com/ultralytics/yolov5
	cd yolov5
	pip install -r requirements.txt

pycocotools:

	pip install git+https://github.com/philferriere/cocoapi.git#subdirectory=PythonAPI



Training
-------------------------------------------------------------------------
To train the models, we first need to put every file into the right directory to ensure the whole process can run normally, and I will specify the steps to handle it below.

	1. Create a directory "pj" first, and move to the "pj" directory 
	
	2. Since this implementation is based on yolov5, run this: git clone https://github.com/ultralytics/yolov5
	
	3. Now we have a yolov5 directory in "pj", next, we create a new directory "data" in "pj".
	
	4. We copy our "train" and "test" directory into "data", they contain train and test images respectively
	
	5. Also put "data_process.py" and "split.py" into "data" directory
	
	6. Run "data_process.py", this would generate labels for the train images and store them into "./labels" directory

	7. Run "split.py", this would split the train data randomly into train and validate part in proportion of 9:1, and the two parts would be properly and automatically seperated into different directories, that you don't need to worry about.
	
	8. Now we have the "data" directory properly set up, next, simply copy "digits.yaml" into the "yolov5" directory
	
	9. All data are now in the right place, and it should look like this, note that if there is no (F) postfix, that is a directory
	
	
	pj ----- yolov5 ---- digits.yaml(F) 
	   |		|
	   |		|
	   |		---- other files in yolov5
	   |
	   ----- data ---- train ---- images
	   	      |          |
		      |		 |
		      |		 ---- labels
		      |
		      ---- val ---- images
		      |	       |
		      |	       |
		      |	       ---- labels
		      |
		      ---- test
		      |
		      |
		      |
		      |
		      ---- data_process.py(F)
		      |
		      |
		      |
		      |
		      ---- split.py(F)

Now we are prepared to train the model.

To train the model, run this command in "yolov5" directory:

	python train.py --img 320 --batch 16 --epochs 120 --data digits.yaml --device 0 --weights yolov5s.pt

You don't need to worry the yolov5s.pt not existed problem, since it would be automatically downloaded when running the command.

This command would perform the training using the pretrained yolov5s model with following hyperparameters:
	
	batch size:16
	resize img: 320*320
	max epochs: 120

You can check the result in the "runs" directory in "yolov5" directory.

Evaluation
-------------------------------------------------------------------------
Two ways to evaluate my model: Locally run it or using Colab

Locally Run:
	To evaluate the model, first download my model from here:
	https://drive.google.com/drive/folders/1n-TN6DMNZlATZjg5U38oLqBmY0Eiz2Cg?usp=sharing

	Put the best.pt into the "yolov5" directory, then run:

		python val.py --img 320 --save-json --data digits.yaml --task test --device 0 --weights best.pt
	

	After running, a file "best_prediction.json" would be generated and stored in the "runs" directory.
    
	Change the filename to "answer.json" and compress it to .zip file and upload to codalab is enough to evaluate my model's prediction
	
Colab:
	You should do the following first to ensure the program can run properly
		
		1. Sign in your google account
		2. Create two directories in your google drive and name them as "VRDL_HW2_config" and "VRDL_HW2_model"
		3. Put best.pt into "VRDL_HW2_model", and put digits.yaml into "VRDL_HW2_config"
		
	Then simply run inference.ipynb step by step, best_predictions.json will be generated and automatically downloaded to your computer.
	
	Same, change its name to answer.json, compress to .zip and submit it to codalab to check the mAP. 
	
For code and data link:

Inference.ipynb: https://colab.research.google.com/drive/1_ziiQF5g-lu8BFIUoYCgF-i9x2s8C_EB?usp=sharing
		
Config(digits.yaml): https://drive.google.com/drive/u/0/folders/1ZJoVoq383pYioPzD-2-CH_OS6z4jK7So
		
Model(best.pt): https://drive.google.com/drive/u/0/folders/1n-TN6DMNZlATZjg5U38oLqBmY0Eiz2Cg


Note: It is kind of weird that I have two different prediction result when running locally and on colab.

When running on COLAB, I have mAP: 0.416198 

When running on local, I have mAP: 0.41623

There's only a minor diff about 0.00003 between them.

I've checked the two files generated, and they're almost the same, both in size and content.

I now have no idea why this goes on, but can only think it as a python version issue, and unfortunately, now I haven't fixed the issue.


	
Pre-trained Models
-------------------------------------------------------------------------
You can download and use pretrained models by simply running training command above:
    
	python train.py --img 320 --batch 16 --epochs 120 --data digits.yaml --device 0 --weights yolov5s.pt

This will download yolov5s.pt if not downloaded yet.
    
    
Results
-------------------------------------------------------------------------
Our model achieves the following performance on :

mAP: HW2 challenge on codalab	

![img1](https://github.com/egghead2630/VRDL_HW2/blob/main/result.png)

benchmark: on Colab

![img2](https://github.com/egghead2630/VRDL_HW2/blob/main/infer_result.png)



Reproducing without retraining
-------------------------------------------------------------------------
Please refer to evaluation part, there is a detailed explaination.





Thanks for reading this README.
