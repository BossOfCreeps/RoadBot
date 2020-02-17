/*
Thomas Sanchez Lengeling.
http://codigogenerativo.com/

KinectPV2, Kinect for Windows v2 library for processing

Depth  and infrared Test
*/

import KinectPV2.*;

KinectPV2 kinect;
int[][] map = new int [103][85];
int map_def=10;

void setup() {
  size(1024, 424, P3D);

  kinect = new KinectPV2(this);
  kinect.enableDepthImg(true);
  kinect.enableInfraredImg(true);
  kinect.enableInfraredLongExposureImg(true);
  kinect.init();
}

void draw() {
  background(0);

  //obtain the depth frame, 8 bit gray scale format
  image(kinect.getDepth256Image(), 0, 0);

  //obtain the depth frame as strips of 256 gray scale values
  image(kinect.getInfraredImage(), 512, 0);

  //raw Data int valeus from [0 - 4500]
  int [] depth = kinect.getRawDepthData();
  
  //image(kinect.getDepth256Image(), 0, 0);




  // обнуление
  loadPixels(); 
  int x3=1000, x4=0, y3=0, y4=0;
  for (int y = 0; y < 22; y++) for (int x = 0; x < 62; x++) map[x][y]=0; 

  // проверка
  for (int y = 5; y < 423; y+=5) {
    for (int x = 5; x < 511; x+=5) {
      int loc = x + y*512;
      if ((abs(depth[loc]-depth[loc-5])>map_def)&&(depth[loc]>520)) { // ! 
        map[(x-5)/5][(y-5)/5]=1;
      }
    }
  }

  // анализ массива
  for (int y = 0; y < 83; y++) 
    for (int x = 0; x < 103; x++) { 
      if ((map[x][y]==1)&&(map[x+1][y]==1)&&(map[x][y+1]==1)&&(y<82)&&(x<102)) {
        if (5+x*5<x3) { 
          x3=x*5+5; 
          y3=y*5+5;
        }
        if (5+x*5>x4) { 
          x4=100+x*5; 
          y4=424*2/3+y*5;
        }
      }
    }
    rect(x3, y3, 10, 10); // дырка

}