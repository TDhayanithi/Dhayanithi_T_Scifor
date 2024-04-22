# 1)What is Transfer learning?

--> Transfer learning is a method of reusing a pre-trained model knowledge for another task. It can be used for classification, regression and clustering problems. It is a long process to collect related training data and rebuild the models. In such cases, Transferring of Knowledge or transfer learning from disparate domains would be desirable.

# 2)What is VGG16?

--> VGG is a Convolutional Neural Network architecture, It was proposed by Karen Simonyan and Andrew Zisserman of Oxford Robotics Institute in the year 2014. It was submitted to Large Scale Visual Recognition Challenge 2014 (ILSVRC2014) and The model achieves 92.7% top-5 test accuracy in ImageNet (dataset). 


# 3)Transfer Learning Using VGG16

--> We can add one more layer or retrain the last layer to extract the main features of our image. We can also give the weight of VGG16 and train again, instead of using random weight (Fine Tuning). Here in this task, we have to do face recognition using transfer learning for the model training. We will use pre-defined weights and will freeze the upper layers or the input layers and will use them as they have weights.

Here, We are going to use VGG16 to train the model.VGG16 is a pre-trained model.

# 4)What is the Pre-trained Model?

A pre-trained model has been previously trained on a dataset and contains the weights and biases that represent 
the features of whichever dataset it was trained on. Learned features are often transferable to different data. 
For example, a model trained on a large dataset of bird images will contain learned features like edges or 
horizontal lines that you would be transferable to your dataset.


# 5)Why use a Pre-trained Model?

Pre-trained models are beneficial to us for many reasons. By using a pre-trained model you are saving time. 
Someone else has already spent the time and compute resources to learn a lot of features and your model will get benefit from these pre-trained weights.

# 6) VGG16:-

VGG16 is a convolution neural net (CNN ) architecture which was used to win ILSVR(Imagenet) competition in 2014. It is considered to be one of the excellent vision 
model architecture till date. Most unique thing about VGG16 is that instead of having a large number of hyper-parameter they focused on having convolution layers of 
3x3 filter with a stride 1 and always used same padding and maxpool layer of 2x2 filter of stride 2. It follows this arrangement of convolution and max pool layers
consistently throughout the whole architecture. In the end it has 2 FC(fully connected layers) followed by a softmax for output. The 16 in VGG16 refers to it has 16 layers 
that have weights. This network is a pretty large network and it has about 138 million (approx) parameters.

# 7) The architecture of VGG16:-

![](https://media.geeksforgeeks.org/wp-content/uploads/20200219152207/new41.jpg)

# NOTE :-
last cell which is used for the real time face recognition
