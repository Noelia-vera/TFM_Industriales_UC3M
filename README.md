# SIMULATION


A simulation of domestic environments has been developed in order to have a digital model that allows the development of the different algorithms. In addition, it is also intended to acquire data from the environment to retrain neural networks and check whether the simulated models are valid for use in the real robot. 

***

## SIMULATORS

The options available in terms of commercial simulators are very varied. Technological advances and constant change in the field mean that new simulators are appearing, while others are becoming obsolete. There is no guide that facilitates the selection of a suitable simulation tool for the specific needs of each researcher. Some of the most prominent simulators in the field of robotics are presented below, detailing their characteristics:
|**SIMULATOR**|**CHRONOS**|**COPPELIASIM**|**GAZEBO**|**ISAAC**|**UNITY**|**WEBOTS**|
|-------------------|----------------|------|------------|--------|-------|-------|
|GPS|V|V|V|V|V|V|
|LIDAR|V|V|V|V|V|V|
|TRACKS|V|V|V|V|V|V|
|WHEELS|V|V|V|V|V|V|
|OMNI WHEELS|V|V|V|V|V|V|
|HEIGHTMAP IMPORT|V|V|V|V|V|V|
|OPENDRIVE|X|X|X|X|X|V|
|OPENSTREETMAP|X|X|X|X|X|V|
|PATHPLANNING|X|V|V|V|X|V|
|ROS SUPPORT|X|V|V|V|X|V|
|RGBD|V|V|V|V|V|V|
|REALISTIC RENDERING|V|V|X|V|V|X|


## METHODOLOGY

This section details the proposed method to generate random domestic environments in the CoppeliaSim simulator. The objective is to generate environment containing realistic household elements ensuring a logical room distribution, and where a robot, in our case the ADAM, can be introduced to operate and perform different applications. 


### GENERATION OF RANDOM DOMESTIC ENVIRONMENTS
The domestic environment is modeled as a 3x3 matrix $A$ divided into cells $(a_{i,j})$ for i,j = 0,1,2 which correspond to a certain area. This ensures a regular house plan that can allocate diverse essential room types (such as kitchens or bathrooms) and wide open spaces. Both the orientation and position of a room must be indicated when generating a room in the simulator. Rooms, and specially the outermost ones divided into \textit{corner rooms} (in contact with two rooms, N=2), \textit{side rooms} (in contact with three rooms, N=3) and \textit{center room} (in contact with four rooms, N=4), must be correctly oriented to avoid placing doors that coincide with external or internal walls. For each cell $a_{i,j}$ we define a set of \textit{connection vectors} $C_{i,j} = [c_{(i,j),0},..., c_{(i,j),N-1}]$, where each \textit{connection} $c_{(i,j),k}$ where $k=0,...,N$, points to the location of an adjacent room. Then, each room model must be rotated to the orientation $\theta_{i,j}$ for which the room's connections $C'_{i,j}$ are aligned with cell connections $C_{i,j}$ of their assigned location. This means that in their proper orientation, the room's connections point to existing rooms, not out of bounds.

[![matrix](../fig/1.png)]

This process is divided in two steps:

* **Random selection of room:** The first part of the method consists on the random selection of room models for each type of room. To generate our environments, each type of room is generated once. Table~\ref{tab:room_types} shows the different room types with their default \textit{connection} vectors to adjacent rooms at $\theta_{i,j} = 0$. Note that type 4 rooms that correspond to living room models are described as large rooms. This type of room occupies two adjacent areas (cells) in any orientation, i.e., $(a_{i,j},a_{i+1,j})$ or $(a_{i,j},a_{i,j+1})$. Type 5 room models are designated to be the center area with fixed position $a_{1,1}$.

|**TYPE**|**DESCRIPTION**|**CONNECTIONS AT $\theta_{i,j}=0$**|
|-------------------|----------------|------|
|0|Hall (Side) |[[0, -1],[-1, 0],[0,1]]|
|1|Kitchen (Corner) |[[0, -1],[-1, 0]]|
|2|Bathroom (Corner)|[[0, -1],[-1, 0]]|
|3|Free use (Side)|[[0, -1],[-1, 0],[0,1]]|
|4|Living room (Side, large)|[[0, -1],[-1, 0],[0,1]]|
|5|Center area|[[0, -1],[-1, 0],[0,1],[1,0]]|
|6|Bedroom (Corner)|[[0, -1],[-1, 0]]|
|7|Office (Side)|[[0, -1],[-1, 0],[0,1]]|


A set of $M_t$ distinct room models in CoppeliaSim are predefined for each room type $t$, so the probability of a model $m_{t,i}$ being selected for a certain type is $P(m_{t,i}|t) = \frac{1}{|M_t|}$. Figure~\ref{fig:example_rooms} shows an example of room models for side and corner rooms, oriented at $\theta = 0\;rad$ and located at the world origin. The result of this part is a set of unique room models identified by their room type $t$ initialized at default position, origin and connections.


* **Random distribution of rooms:**  The second part of the method consist in the random distribution of the rooms shown in Algorithm~\ref{alg:random_rooms}. We define a vector $T_{1 \times 8}$ where each of its elements $T_t$ contains the randomly selected room model $m_{t}$ and its corresponding connections $C'_{i,j}$ for each room type $t=0,...,7$. The elements in $T$ are randomly shuffled and assigned to empty cells in the area distribution matrix $A = (a_{i,j})_{3\times 3}$ according to their room type. It is also ensured that the room connections $C'_{i,j}$ align with their corresponding cell connections (pointing to not out of bounds existing areas) and rotated otherwise with a rotation matrix $R_z(\pi/2)$ and $\theta_{i,j} = \theta_{i,j} + \pi/2 \;rad$. Other restrictions imposed are the location of the center room in cell $a_{1,1}$ and the assignation of two adjacent cells to large rooms as previously mentioned in this Section.

Having assigned the rooms to each area cell, the models are placed and oriented in the empty scene in CoppeliaSim to which the algorithm is connected. The models are placed at the coordinates given by $a_{i,j}$ times the room length of a cell $d = 5$ m and oriented at their corresponding angle $\theta_{i,j}$ with respect to the world's reference frame.

[![example](../fig/2.png)]

The algorithm is not only responsible for placing the rooms in certain positions, but also for orienting them in such a way that they do not generate discontinuities or failures in the design.


[![example](../fig/7.png)]

### EXAMPLES OF THE ROOMS

The following are examples of individually designed rooms for the generation of a complete environment.

[![room](../fig/3.png)]
[![room](../fig/4.png)]
[![room](../fig/5.png)]


Several complete simulation environments have been generated where the rooms comply with the appropriate positions and orientations indicated in the matrix.

[![environments](../fig/6.png)]

***

### MOBILE ROBOT

The robot used in this work is the Autonomous Domestic Ambidextrous Manipulator (ADAM), designed by the Mobile Robots laboratory, part of the Robotics Lab at Universidad Carlos III de Madrid. The laboratory collaborated with the company Robotnik to manufacture the robot based on the specifications it developed. This autonomous mobile robot with bimanipulation capabilities has been specifically designed to perform domestic tasks, offering support to elderly people in their homes. This makes it a unique robot in the market, with specific functions that only it can perform.

It is composed of a perception system, a mobile base, a torso, two arms, and two grippers, reaching a total height of 160 cm and a width of 50 cm when the arms are at rest. Its design is modular and independent, allowing each part to be worked on separately or jointly, thus expanding the robot's future capabilities. It is divided into four parts:


* **Perception System:** Responsible for capturing information from the environment to manipulate objects and navigate. It includes an RGBD camera and a 2D LiDAR located near the ground. The Realsense D435 RGBD depth camera features an infrared stereo vision module and a traditional RGB module. Its specifications are a maximum resolution of 1280×720 for the depth stream and 1920×1080 for the RGB stream, with a frame rate of 90 and 30 fps, respectively, and a field of view of 87$^{\circ} \times 58^{\circ}$, with an operating range of up to 3 m. Additionally, it has an Ouster OS0 LiDAR sensor to provide a wider angle and range, so that a single scan can capture complete information of the room.

* **Mobile base:**: This platform is the RB-1 model manufactured by the company \textit{Robotnik}\~\\cite{Robotnik}, with dimensions of 50 cm in diameter, two motorized wheels, and three support casters. In this way, the robot can move forward, backward, and rotate on itself, although it cannot move laterally.

* **Dual-arm System:** Due to the need to equip the robot with collaborative arms, the UR3 model from \textit{Universal Robots}\~\\cite{UR} was selected for both arms. Each arm has a total length of 50 cm and a maximum payload capacity of 3 kg. Each arm consists of 6 degrees of freedom (DoF) with a range of motion of ±360$^{\circ}$, except for the end-effector, which allows for more than one full rotation.

* **Robotic Hands:** A parallel-jaw gripper called the \textit{Duck Gripper} was designed, equipped with its own power supply to make it modular and independent of the system. The gripper has a total height of 180 mm and a width of 118 mm measured at its body, and a total width of 148 mm measured at the outer faces of the jaws when the gripper is fully open. These dimensions prevent self-collision between the gripper and the arm. The maximum aperture between the jaws is 117 mm, and the minimum is 35 mm.



The model used in the simulation was generated by the company Robotnik, which was responsible for assembling the real robot according to the specified requirements. The simulated robot is in .urdf (Unified Robot Description Format) format, an XML file type used to describe the structure of robot joints and links in virtual environments.The Figure shows the robot in Gazebo with the local reference frames of its different joints. The compatibility of this file type is direct with Gazebo, but the same is not true for the CoppeliaSim simulator, as it has its own file format for models and robots. It was necessary to convert the format so that the simulator could handle all the functionalities the initial model had, including joint dynamics, physical properties, and reference frames. Finally, it is shown the robot simulated in CoppeliaSim.

# DATA COLLECTION FOR DATASET GENERATION
Data collection is carried out through images of the simulated environment, which are captured by a perspective vision sensor on the simulated robot model. Its configuration consists of a resolution of 640 x 480 pixels with a perspective angle of 50°, allowing control over the robot's field of view within the scene. This sensor is configured with a script that allows taking photos every second during the simulation. Additionally, a path has been generated for the areas of interest that is distributed throughout the space,which the robot follows while simultaneously taking photos. Moreover, this path can be modified in real-time moving the waypoints that define the path if more data is needed from specific areas. a complete scenario generated with the robot is shown, including the range of the vision sensor and the path it must follow for data collection.

## Synthetic dataset generation
Once all the images are saved, they are uploaded to the Roboflow tool. Roboflow is a very versatile application, as it not only allows image labeling but also supports instance and semantic segmentation, object detection, classification, and keypoint detection. In each image, the objects to be labeled are selected, their edges are precisely delineated, and any incorrect assignments are removed to avoid erroneous detections. Each selection is assigned a class, and once the labeling stage is complete, a dataset is created. It is shown the object classification, and display the objects classified by layers, with colors corresponding to their assigned classes.

In this case, data augmentation was performed using spatial transforming: a -15°up to 15° rotation of the images, conversion of 16\% of the images to grey scale and a blur of up to 2.5 pixels. Another data augmentation has been performed locally for pixel-level transformations with the Albumentations library. Changes were made to the hue and saturation values, as well as random brightness contrast and a channel shuffle.

# Experiments and Results
In this section, two aspects will be evaluated: the successful random generation of simulations and the success of detections by a neural network using the generated synthetic images.

## Success in the random generation of environments

Five different models of each type of room have been generated in CoppeliaSim. Although the matrix structure is designed for cells with dimensions of $5 \times 5$ m, some models are purposely designed with larger dimensions ($5 \times 6$ m) and smaller ones ($5 \times 4$ m and $4 \times 3$ m) to demonstrate that the designed method is modular and scalable to different sizes as needed. This results in a total of $5^8 \times 3! \times 4! = 56,250,000$ possible combinations of home environments.


Moreover, although the models were initially designed to be fully furnished with a high degree of detail and objects of interest, semi-furnished models (which include main furniture such as tables, wardrobes, or chairs) and unfurnished models (only essential structural elements like walls, floors, and doors) have been simultaneously designed to study the impact of complexity on execution and generation times.

Tests were conducted with 20 domestic environments generated for each of the three versions of the models, recording the execution time for each and evaluating whether the environment was fully generated. The experiment was conducted on an MSI Katana GF66 with a 12th Gen Intel(R) Core(TM) i7-12700H using CoppeliaSim version 4.5. It can be observed that the level of detail in the rooms is a key factor that increases not only the time required to generate a complete environment but also the number of environments that fail to generate or are incomplete, also it illustrates an incomplete environment where one of the rooms has not been properly oriented and positioned. It is also shown an example of discontinuities in the walls, leading to a design failure by changing the dimensions of the cells.



## Evaluation of successful object detection with a convolutional neural network
A total of 25 classes were used within the 2,177 images randomly generated with the simulated environments, of which 70\% have been used for training, 20\% for validation and 10\% for testing. Augmented data has also been used to expand the database, resulting in a total of 18,904 images.
The amount of generated data is relevant for selecting the neural network to work with. In the case of the YOLOv8 network, there are five possibilities, and the differences between them are the number of parameters and FLOPs (B) they handle. For our case, initial training has been carried out with the YOLOv8n, YOLOv8m, and YOLOv8x networks configured with the same hyperparameters. The YOLOv8n network has been selected because the number of parameters and FLOPs it handles aligns well with the simulated data we are working with. Subsequently, six different trainings of 300 epochs were performed with pre-trained networks, modifying hyperparameters to improve performance metrics such as lr0, lrf, weight decay, dropout, warmup epoch, warmup momentum, warmup bias, and data augmentation parameters such as mosaic, HSV, or crop fraction. The network comprises 195 layers, and during training, a validation phase is performed for each epoch, where the errors, accuracies, and learning of the network are adjusted.

It took 8 hours and 44 minutes to retrain the neural networks with the synthetically generated and hand-labeled images using an Intel i9 12900K CPU and a NVIDIA 3080 GPU with 10GB of VRAM. It is displays the values from the last and best training of the neural network. The mask (Precision) value indicates detection accuracy, while R (recall) represents the proportion of correct detections made by the network on all objects in the image. mAP50 (mean average precision at IoU=0.5) is the average precision across all classes, and mAP50-95 (mean average precision at IoU=0.5 to 0.95) provides a more comprehensive evaluation of the model's performance.



It is illustrates the results of the different training sessions for the most relevant metrics. In general, the detection results exceed 80\% for most classes, while in other specific classes, such as sink or shelf, the detections are around 40\%. This lower performance is attributed to their complex geometry or color, which can lead to confusion with other objects. In contrast, classes like person or bathtub exhibit nearly 100\% detection accuracy, as these classes are already included in the COCO dataset, allowing the network to distinguish these objects very well. Training 6 has proven to be the most successful as it prevents the network from overtraining and overlearning. The value of mAP50-95 for the entire dataset is 0.70, while the official detection accuracy given by YOLOv8n is 0.35, indicating that the accuracy of the detections made by the retrained network with the additional dataset we included is twice as high. It is presented some examples of the results obtained in the tests, where the network identifies objects in images it has not previously seen. It is show an environment with many objects where all classes with high confidence values have been identified. The network is able to differentiate between occluded or small objects in the background. It is also illustrate detections for an image with fewer classes. As before, the detections for all objects exhibit a high degree of confidence, and objects with repeated classes or partial views are identified individually.


# Conclusions and Future Work
This paper presents the collection of data from indoor domestic environments obtained by random generation in the CoppeliaSim simulator. Our goal is to cope with the reduced number of information from domestic environments to solve the difficulties that assistive robots suffer when testing in realistic environments is required.  The algorithm generates a large number of random scenarios by posing the space as a matrix divided into cells representing each room of interest. The results show the versatility of the modular and flexible design, which can be scaled to different room dimensions. In addition, the high correlation between the high generation times of environments versus the degree of detail they present is shown, not always obtaining a complete successful generation for fully furnished environments while the percentage of success is higher in semi-furnished or unfurnished environments.
On the other hand, the images have been manually labeled with classes specific to our application. A simulated dataset has been generated, which has been augmented with tools suitable for use by the YOLOv8 network. The confidence range in the prediction of synthesized objects is very high, successfully classifying occluded or very small objects. The re-trained network can also identify more than ten objects within a single image, accurately defining the bounding boxes without complications. As a final comparison, the results indicate that the confidence in the prediction of objects is twice as high as the official data from the COCO dataset.


As future work, methods will be studied to reduce the generation time of the environments and guarantee the success of the generations. More individual room models will be created to add objects of the same classes with different geometric aspects and colors. In addition, images from the synthetic dataset will be expanded, as well as looking for an automatic labeling method to reduce the time on labeling each object individually. The detection of the network will be checked with real data obtained by the robot to validate the results of this work.

# ARTICLES


[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/COPPELIA.png)

[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Estructura.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2012.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2013.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2014.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2018.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2019.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2020.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2021.png)
[imagenes](https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2023.png)
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2024.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2029.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2030.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2048.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2056.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2059.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2057.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Frame%2060.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/Grafico.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/H1.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/completo.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/final_result.png
çhttps://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/final_results.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/robot_operation.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/robot_vision.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/wrong_walls.png
https://github.com/Noelia-vera/TFM_Industriales_UC3M/blob/main/imagenes/robotflow.png

Este proyecto es una implementación recogida en: [Fernandez, N., Espinoza, G., Mendez, A., Prados, A., Mora, A., & Barber, R. (2024, November). Data Generation in Simulated Domestic Environments for Assistive Robots. In 2024 7th Iberian Robotics Conference (ROBOT) (pp. 1-6). IEEE.](https://ieeexplore.ieee.org/abstract/document/10797352) y en [Fernandez, N., Espinoza, G., Mendez, A., Mora, A., & Barber, R. (2024, May). Simulation of randomly generated domestic environments for assistive robotics. In 2024 IEEE International Conference on Autonomous Robot Systems and Competitions (ICARSC) (pp. 28-33). IEEE.](https://ieeexplore.ieee.org/abstract/document/10535940)