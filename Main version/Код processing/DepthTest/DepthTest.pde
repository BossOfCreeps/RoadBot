import KinectPV2.*; //<>//

KinectPV2 kinect;
int [] depth;
void setup() {
  size(512, 424);

  kinect = new KinectPV2(this);
  kinect.enableDepthImg(true);
  kinect.enableInfraredImg(true);
  kinect.enableInfraredLongExposureImg(true);
  kinect.init();

  thread("GC");
}



void draw() {
  depth = kinect.getRawDepthData();

  loadPixels(); 
  image(kinect.getDepth256Image(), 0, 0);

  for (int y = 200; y < height; y+=5) {
    boolean first=true;  
    int x1=0, x2=0;
    for (int x = 6+100; x < width-100; x+=5) {
      int loc = x + y*width;
      //println(loc);
      if (abs(depth[loc]-depth[loc-5])>75) {
        if (first) {
          first=false;
          x1=x;
        }
        x2=x;
      }
    }

    stroke(255, 0, 0);
    line(x1, y, x2, y+1);
  }
}

void mouseClicked() {

  // x=mouseX;
  print(depth[mouseX+512*260]);
}


void GC() {
  System.gc();
}

/*int dept1h(int a) {
 // return (int) red(kinect.getDepth256Image().pixels[a]);
 return 1;//rawData[a];
 }
 
 int mouse() {
 return mouseX+mouseY*512;
 }
 //      pixels[loc] =  color(r,g,b);          
 
 
 //obtain the depth frame, 8 bit gray scale format
 //  image(kinect.getDepthImage(), 0, 0);
 
 //obtain the depth frame as strips of 256 gray scale values
 
 //if (r>0) println(r);
 
 //infrared data
 //image(kinect.getInfraredImage(), 0, 424);
 //image(kinect.getInfraredLongExposureImage(), 512, 424);
 
 //raw Data int valeus from [0 - 4500]
 
 //values for [0 - 256] strip
 //int [] rawData256 = kinect.getRawDepth256Data();
 
 //stroke(255);
 // text(frameRate, 50, height - 50);
 */