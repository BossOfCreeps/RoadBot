import processing.video.*;
import processing.net.*;
import javax.imageio.*;
import java.awt.image.*; 
import java.io.*;
import java.net.*;
import KinectPV2.*;
KinectPV2 kinect;
DatagramSocket ds; 
Capture cam;

String ad = "192.168.1.35";
//String ad = "127.0.0.1";
//String ad = "10.0.0.19";
//String ad = "25.12.173.173"; //клиент

PImage kinectFrame=createImage(512, 424, RGB);

boolean show=true;
int clientPort = 9010; 
int x1=0, x2=0, y1=0, y2=0;
int[][] map = new int [63][23];
Server s;
Client c;
String input="1";

void setup() {
  size(512, 424);
  frameRate(5);

  //потоки
  thread("GC");
  thread("find");

  s = new Server(this, 12345);

  kinect = new KinectPV2(this);
  kinect.enableDepthImg(true);
  kinect.enableInfraredImg(true);
  kinect.enableColorImg(true);
  kinect.init();

  try {
    ds = new DatagramSocket();
  } 
  catch (SocketException e) {
    e.printStackTrace();
  }
}


void draw() {

  switch (input) {
  case "0": 
    kinectFrame.resize(1304, 1080);
    kinectFrame = kinect.getColorImage().get(308, 0, 1304, 1080);  //камера
    kinectFrame.resize(512, 424);
    break; 
  case "1": 
    kinectFrame.resize(512, 424);
    kinectFrame = kinect.getDepth256Image();                       // крутая карта глубины  
    break; 
  case "2": 
    kinectFrame.resize(512, 424);
    kinectFrame = kinect.getDepthImage();                          // стремная карта глубины
    break; 
  case "3": 
    kinectFrame.resize(512, 424);
    kinectFrame = kinect.getInfraredImage();                       // инфракрасное зрение
    break;
  }                                                                //kinect.getRawDepth256Data()
  broadcast(kinectFrame);
  image(kinectFrame, 0, 0);

  if (mousePressed == true) {
    s.write("1");
  }

  c = s.available();

  if (c != null) {
    input = c.readString();
    println(input);
  }



}

void mousePressed() {
  int [] depth = kinect.getRawDepthData();

  print(depth[mouseX+mouseY*512]);
}



void GC() {
  System.gc(); 
  delay(100);
}

void setcolor(int r, int g, int b) {
  stroke(r, g, b);      
  fill(r, g, b);
}
void broadcast(PImage img) {
  BufferedImage bimg = new BufferedImage( img.width, img.height, BufferedImage.TYPE_INT_RGB );

  img.loadPixels();
  bimg.setRGB(0, 0, img.width, img.height, img.pixels, 0, img.width);

  ByteArrayOutputStream baStream = new ByteArrayOutputStream();
  BufferedOutputStream bos = new BufferedOutputStream(baStream);

  try {
    ImageIO.write(bimg, "jpg", bos);
  } 
  catch (IOException e) {
    e.printStackTrace();
  }

  byte[] packet = baStream.toByteArray();

  try {
    ds.send(new DatagramPacket(packet, packet.length, InetAddress.getByName(ad), clientPort));
  } 
  catch (Exception e) {
    e.printStackTrace();
  }
}