# Frontier-Project (Pelita Harapan University)
## Traffic Light Analysis
**Data Source:**
> [LISA Traffic Light Dataset](https://www.kaggle.com/mbornoe/lisa-traffic-light-dataset)


**Team Member:**
  - _Bong Cen Choi_
  - _Gabriel Dejan P._
  - _Joshua Kaven K._

### Content
The database is collected in San Diego, California, USA. The database provides four day-time and two night-time sequences primarily used for testing, providing 23 minutes and 25 seconds of driving in Pacific Beach and La Jolla, San Diego. The stereo image pairs are acquired using the Point Grey’s Bumblebee XB3 (BBX3-13S2C-60) which contains three lenses which capture images with a resolution of 1280 x 960, each with a Field of View(FoV) of 66°. Where the left camera view is used for all the test sequences and training clips. The training clips consists of 13 daytime clips and 5 nighttime clips.

### Annotations
The annotation.zip contains are two types of annotation present for each sequence and clip. The first annotation type contains information of the entire TL area and what state the TL is in. This annotation file is called frameAnnotationsBOX, and is generated from the second annotation file by enlarging all annotation larger than 4x4. *The second one is annotation marking only the area of the traffic light which is lit and what state it is in*. This second annotation file is called **frameAnnotationsBULB**.

The annotations are stored as 1 annotation per line with the addition of information such as class tag and file path to individual image files. With this structure the annotations are stored in a csv file, where the structure is exemplified in below listing:

Filename;Annotation tag;Upper left corner X;Upper left corner Y;Lower right corner X;Lower right corner Y;Origin file;Origin frame number;Origin track;Origin track frame number

### Dataset used in this project: 
 Annotation file **frameAnnotationsBULB**


### Acknowledgements
> Jensen MB, Philipsen MP, Møgelmose A, Moeslund TB, Trivedi MM. Vision for Looking at Traffic Lights: Issues, Survey, and Perspectives. I E E E Transactions on Intelligent Transportation Systems. 2016 Feb 3;17(7):1800-1815. Available from, DOI: 10.1109/TITS.2015.2509509

> Philipsen, M. P., Jensen, M. B., Møgelmose, A., Moeslund, T. B., & Trivedi, M. M. (2015, September). Traffic light detection: A learning algorithm and evaluations on challenging dataset. In intelligent transportation systems (ITSC), 2015 IEEE 18th international conference on (pp. 2341-2345). IEEE.
