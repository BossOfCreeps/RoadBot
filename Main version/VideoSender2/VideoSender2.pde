// библиотеки
import processing.video.*;
import processing.net.*;

import javax.imageio.*;
import java.awt.image.*; 
import java.io.*;
import java.net.*;
import KinectPV2.*;

// библиотчные переменные
KinectPV2 kinect;
DatagramSocket ds; 
Capture cam;
Server s;
Client c;

// важно
int step=3;
int map_def=10;
boolean show=true;  
//String ad = "192.168.137.84";
//String ad = "192.168.1.33"; // приёмник (tablet)
String ad = "localhost";
//String ad = "172.20.33.161";
//String ad = "10.0.0.19";
//String ad = "25.17.78.44";

int clientPort = 9010; 
int x1=0, x2=0, y1=0, y2=0;
int[][] map = new int [63][23];
String input="0";

PImage All = createImage(512, 424, RGB);
PImage Color = createImage(1920, 1080, RGB);
PImage Depth = createImage(512, 424, RGB);
PImage Depth256 = createImage(512, 424, RGB);
PImage Infrared = createImage(512, 424, RGB);

boolean[][] redMap = new boolean[500][500]; 
float[][] point =new float [7][2];
boolean[] pointB =new boolean [7];

int[] red =       { 124, 37, 13, 20 };
int[] white =     { 157, 173, 184, 100 };
int[] black =     {  25, 25, 25, 100 };

int[] redON =     { 252, 176, 152, 30 };
int[] yellowON =  { 255, 255, 255, 10 };
int[] greenON =   { 36, 250, 237, 20 };
int[] greenON1 =  { 70, 252, 252, 20 };
int[] greenON2 =  { 80, 250, 239, 20 };
int[] redOFF =    { 233, 53, 87, 20 };
int[] yellowOFF = { 247, 233, 84, 20 };
int[] greenOFF =  {  74, 175, 145, 50 };

int helpX=1;
int helpY=1;

int top=100000;
int bot=0;
int rig=0;
int lef=100000;

void setup() {
  size(960, 803);
  frameRate(5);

  //потоки
  thread("GC");
  thread("Stream");

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
  image(All, 0, 0);

  /// ВЫВОД ИЗОБРАЖЕНИЙ \\\

  Color.resize(1920, 1080);
  Color=kinect.getColorImage();
  Color.resize(960, 540);

  Depth.resize(512, 424);
  Depth=kinect.getDepth256Image();
  Depth.resize(320, 265);

  Depth256.resize(512, 424);
  Depth256=kinect.getDepthImage();
  Depth256.resize(320, 265);

  Infrared.resize(512, 424);
  Infrared=kinect.getInfraredImage();
  Infrared.resize(320, 265);

  All.copy(Color, 0, 0, 960, 540, 0, 0, 960, 540);
  All.copy(Depth, 0, 0, 320, 265, 0, 540, 320, 265);
  All.copy(Depth256, 0, 0, 320, 265, 320, 540, 320, 265);
  All.copy(Infrared, 0, 0, 320, 265, 640, 540, 320, 265);

  /*pushMatrix();
   scale(-1, 1);
   image(All, -960, 0);
   popMatrix(); */



  /// ПОИСК ЗНАКА \\\

  loadPixels(); 
  Color.loadPixels();

  boolean foundZnak=false;
  for (int y = 0; y < Color.height; y+=step) 
    for (int x = 0; x < Color.width-720; x+=step) {
      if (compare(Color, x + y*Color.width, red[0], red[1], red[2], red[3])) {
        foundZnak=true;
        redMap[x/step][y/step]=true;
      } else { 
        redMap[x/step][y/step]=false;
      }
    }

  if (foundZnak) {
    top=100000;
    bot=0;
    rig=0;
    lef=100000;

    for (int y = 1; y < 539/step; y++) 
      for (int x = 1; x < 959/step; x++) {
        if ((redMap[x][y])&&(redMap[x+1][y])&&(redMap[x][y+1])&&(redMap[x-1][y])&&(redMap[x][y-1])) {
          if (x*step<lef)lef=x*step;
          if (x*step>rig)rig=x*step;
          if (y*step<top)top=y*step;
          if (y*step>bot)bot=y*step;
        }
      }
    helpX=0;
    helpY=0;
    int centerX=(rig+lef)/2;
    int centerY=(bot+top)/2;
    if ((centerX<960)&&(centerY<540)) {
      while (compare(Color, centerX+(centerY+helpY)*Color.width, white[0], white[1], white[2], white[3])) helpY++;
      while (compare(Color, centerX+helpX+centerY*Color.width, white[0], white[1], white[2], white[3])) helpX++;
      if ((helpX>0)&&(helpY>0)) {
        int speedHelp=0, speedHelp2=0, speedHelp3=0;
        for (int i=0; i<2; i++) { 
          while (compare(Color, centerX-speedHelp+centerY*Color.width, white[0], white[1], white[2], white[3])) speedHelp++;
          while (compare(Color, centerX-speedHelp+centerY*Color.width, black[0], black[1], black[2], black[3])) speedHelp++;
        }

        while (compare(Color, centerX-speedHelp/2+(-speedHelp2+centerY)*Color.width, white[0], white[1], white[2], white[3])) speedHelp2++;
        while (compare(Color, centerX-speedHelp/2+(-speedHelp2+centerY)*Color.width, black[0], black[1], black[2], black[3])) speedHelp2++;

        while (compare(Color, centerX-speedHelp/2+(speedHelp3+centerY)*Color.width, white[0], white[1], white[2], white[3])) speedHelp3++;
        while (compare(Color, centerX-speedHelp/2+(speedHelp3+centerY)*Color.width, black[0], black[1], black[2], black[3])) speedHelp3++;

        point[0][0]=centerX+speedHelp/2;
        point[0][1]=centerY-speedHelp2+4;
        point[1][0]=centerX+6;
        point[1][1]=centerY-speedHelp2/2+2;
        point[2][0]=centerX+speedHelp-6;
        point[2][1]=centerY-speedHelp2/2+2;
        point[3][0]=(centerX+(speedHelp/2))*1.025;
        point[3][1]=(2*centerY-speedHelp2+speedHelp3)/2;
        point[4][0]=centerX+12;
        point[4][1]=centerY+speedHelp3/2+2;
        point[5][0]=centerX+speedHelp;
        point[5][1]=centerY+speedHelp3/2+2;
        point[6][0]=(centerX+(speedHelp/2))*1.05;
        point[6][1]=centerY+speedHelp3-4;
        try {
          for (int i=0; i<8; i++) pointB[i]=compare(Color, point[i][0]+point[i][1]*Color.width, black[0], black[1], black[2], black[3]);
        }
        catch (Exception e) {
        }
      }
    }
  }


  int road_marking_x = 900;
  int road_marking_y = 500;
  int road_marking_d = 20;
  boolean road_marking_1 = false;
  boolean road_marking_2 = false;
  boolean road_marking_3 = false;
  /// ПОИСК РАЗМЕТКИ \\\

  if (compare(Color, road_marking_x-road_marking_d+road_marking_y*(Color.width), black[0], black[1], black[2], black[3])) road_marking_1=true;
  if (compare(Color, road_marking_x+road_marking_y*(Color.width), black[0], black[1], black[2], black[3]))                road_marking_2=true;
  if (compare(Color, road_marking_x+road_marking_d+road_marking_y*(Color.width), black[0], black[1], black[2], black[3])) road_marking_3=true;

  /// ПОИСК СВЕТОФОРА \\\
  int greenX=0, greenY=0, redY=0, yellowY=0, greenC=0, helpGX=0, helpGY=0, helpGx=0, helpGy=0, helpRy=0, helpRY=0, helpYy=0, helpYY=0, helpGup=0; 
  for (int y = 100; y < Color.height-10; y+=step) 
    for (int x = 10; x < Color.width-720; x+=step) {
      if ((ultraCompare(Color, x+y*(Color.width), greenOFF[0], greenOFF[1], greenOFF[2], greenOFF[3]+5))||
        (compare(Color, x+y*(Color.width), greenON1[0], greenON1[1], greenON1[2], greenON1[3]))||
        (compare(Color, x+y*(Color.width), greenON2[0], greenON2[1], greenON2[2], greenON2[3]))||
        (compare(Color, x+y*(Color.width), greenON[0], greenON[1], greenON[2], greenON[3]))) {
        greenX+=x;
        greenY+=y;
        greenC++;
        // ellipse(x, y, 2, 2);
      }
    }
  if (greenC>3) {
    greenX=greenX/greenC-1;
    greenY=greenY/greenC-1;
    int gR=0, gG=0, gB=0, gA=0, dop=0;
    boolean rON=false, gON=false, yON=false;
    if (ultraCompare(Color, greenX+greenY*(Color.width), greenOFF[0], greenOFF[1], greenOFF[2], greenOFF[3])) {
      gR=greenOFF[0];
      gG=greenOFF[1];
      gB=greenOFF[2];
      gA=greenOFF[3];
      dop=0;
    } else {
      gR=greenON[0];
      gG=greenON[1];
      gB=greenON[2];
      gA=greenON[3];
      dop=0;
    }
    while (compare(Color, (greenX+helpGX)+greenY*Color.width, gR, gG, gB, gA)) helpGX++; 
    while (compare(Color, (greenX+helpGx)+greenY*Color.width, gR, gG, gB, gA)) helpGx--;
    while (compare(Color, greenX+(helpGY+greenY)*Color.width, gR, gG, gB, gA)) helpGY++;
    while (compare(Color, greenX+(helpGy+greenY)*Color.width, gR, gG, gB, gA)) helpGy--;

    greenX=greenX+(helpGX+helpGx)/2;
    greenY=greenY+(helpGY+helpGy)/2;

    helpGup=0;
    while ((!(compare(Color, greenX+(helpGup+greenY)*Color.width, black[0], black[1], black[2], black[3]+dop)))&&(-helpGy<greenY)) helpGup--; //до верхнего края зелёного
    //ellipse(greenX, greenY+helpGy, 2, 2);
    helpYY=helpGup;
    while ((compare(Color, greenX+(helpYY+greenY)*Color.width, black[0], black[1], black[2], black[3]+dop))&&(-helpYY<greenY)) helpYY--;    //до нижнего края желтого
    //ellipse(greenX, greenY+helpYY, 2, 2);
    helpYy=helpYY;
    while ((!(compare(Color, greenX+(helpYy+greenY)*Color.width, black[0], black[1], black[2], black[3]+dop)))&&(-helpYy<greenY)) helpYy--; //до верхнего края красного
    //ellipse(greenX, greenY+helpYy, 2, 2);
    helpRY=helpYy;
    while ((compare(Color, greenX+(helpRY+greenY)*Color.width, black[0], black[1], black[2], black[3]+dop))&&(-helpRY<greenY)) helpRY--;    //до нижнего края красного
    //ellipse(greenX, greenY+helpRY, 2, 2);
    helpRy=helpRY;
    while ((!(compare(Color, greenX+(helpRy+greenY)*Color.width, black[0], black[1], black[2], black[3]+dop)))&&(-helpRy<greenY)) helpRy--; //до верхнего края красного
    //ellipse(greenX, greenY+helpRy, 2, 2);

    yellowY=greenY+(helpYy+helpYY)/2;
    redY=greenY+(helpRy+helpRY)/2;

    if (compare(Color, greenX+redY*(Color.width), redOFF[0], redOFF[1], redOFF[2], redOFF[3]+20)) rON=false; 
    else rON=true; 
    if (compare(Color, greenX+yellowY*(Color.width), yellowON[0], yellowON[1], yellowON[2], yellowON[3])) yON=true; 
    else yON=false; 
    if (compare(Color, greenX+greenY*(Color.width), greenOFF[0], greenOFF[1], greenOFF[2], greenOFF[3]+10)) gON=false; 
    else gON=true; 

    if (gON) strokeWeight(4); 
    else strokeWeight(1);
    stroke(0, 255, 0);   
    ellipse(greenX, greenY, (greenY-yellowY), (greenY-yellowY));

    if (yON) strokeWeight(4); 
    else strokeWeight(1);
    stroke(255, 255, 0);   
    ellipse(greenX, yellowY, (greenY-yellowY), (greenY-yellowY));

    if (rON) strokeWeight(4); 
    else strokeWeight(1);
    stroke(255, 0, 0);   
    ellipse(greenX, redY, (greenY-yellowY), (greenY-yellowY));
    strokeWeight(1);
    //rect(greenX+helpGx,greenY+helpRy,-helpGX+helpGx,helpGY-helpRy);
    //println(rON, " ", yON, " ", gON);
  }


  /// ПОИСК ЯМЫ \\\

  //image(kinect.getDepth256Image(), 0, 0);
  int [] depth = kinect.getRawDepthData();

  // обнуление
  loadPixels(); 
  int x3=1000, x4=0, y3=0, y4=0;
  for (int y = 0; y < 22; y++) for (int x = 0; x < 62; x++) map[x][y]=0; 

  // проверка
  for (int y = 424*2/3; y < 424-30; y+=5) {
    for (int x = 100; x < 512-100; x+=5) {
      int loc = x + y*512;
      if ((abs(depth[loc]-depth[loc-5])>map_def)&&(depth[loc]>520)) { // ! 
        map[(x-100)/5][(y-424*2/3)/5]=1;
      }
    }
  }

  // анализ массива
  for (int y = 0; y < 22; y++) 
    for (int x = 0; x < 62; x++) { 
      if ((map[x][y]==1)&&(map[x+1][y]==1)&&(map[x][y+1]==1)&&(y<21)&&(x<61)) {
        if (100+x*5<x3) { 
          x3=100+x*5; 
          y3=424*2/3+y*5;
        }
        if (100+x*5>x4) { 
          x4=100+x*5; 
          y4=424*2/3+y*5;
        }
      }
    }



  /// РИСОВАНИЕ \\\

  noFill();   
  stroke(255, 0, 0);

  rect(0, 0, 960-721, 539);
  if (rig>lef) rect(lef-10, top-10, rig-lef+20, bot-top+20); // знак
  if (y3>0) ellipse((x4+x3)/2/1.6, 540+(y4+y3)/2/1.6, 10, 10); // дырка
  rect(100/1.6, 540+424*2/3/1.6, (512-200)/1.6, (424/3-30)/1.6);
  try {
    for (int i=0; i<7; i++) if (pointB[i]) ellipse( point[i][0]-2, point[i][1]-2, 4, 4);
  }
  catch (Exception e) {
  }

  if (helpX>helpY) text("stop", lef-10, top-10);
  if ((!pointB[0])&&( pointB[1])&&(!pointB[2])&&(!pointB[3])&&( pointB[4])&&(!pointB[5])&&(!pointB[6])) text("1", 100, 100);
  if (( pointB[0])&&( pointB[1])&&(!pointB[2])&&( pointB[3])&&(!pointB[4])&&( pointB[5])&&( pointB[6])) text("2", 100, 100);
  if (( pointB[0])&&( pointB[1])&&(!pointB[2])&&( pointB[3])&&( pointB[4])&&(!pointB[5])&&( pointB[6])) text("3", 100, 100);
  if ((!pointB[0])&&( pointB[1])&&( pointB[2])&&( pointB[3])&&( pointB[4])&&(!pointB[5])&&(!pointB[6])) text("4", 100, 100);
  if (( pointB[0])&&(!pointB[1])&&( pointB[2])&&( pointB[3])&&( pointB[4])&&(!pointB[5])&&( pointB[6])) text("5", 100, 100);
  if (( pointB[0])&&(!pointB[1])&&( pointB[2])&&( pointB[3])&&( pointB[4])&&( pointB[5])&&( pointB[6])) text("6", 100, 100);
  if (( pointB[0])&&( pointB[1])&&(!pointB[2])&&(!pointB[3])&&( pointB[4])&&(!pointB[5])&&(!pointB[6])) text("7", 100, 100);
  if (( pointB[0])&&( pointB[1])&&( pointB[2])&&( pointB[3])&&( pointB[4])&&( pointB[5])&&( pointB[6])) text("8", 100, 100);
  if (( pointB[0])&&( pointB[1])&&( pointB[2])&&( pointB[3])&&( pointB[4])&&(!pointB[5])&&( pointB[6])) text("9", 100, 100);
  if (( pointB[0])&&( pointB[1])&&( pointB[2])&&(!pointB[3])&&( pointB[4])&&( pointB[5])&&( pointB[6])) text("0", 100, 100);

  if (road_marking_1) fill(255,0,0); else noFill();
  ellipse(road_marking_x-road_marking_d, road_marking_y, 10, 10); 
  
  if (road_marking_2) fill(255,0,0); else noFill();
  ellipse(road_marking_x, road_marking_y, 10, 10); 
  
  if (road_marking_3) fill(255,0,0); else noFill();
  ellipse(road_marking_x+road_marking_d, road_marking_y, 10, 10); 

  /// СТРИМИНГ \\\

  All.resize(800, 600);
  //All.resize(512, 424);
  broadcast(All);
  All.resize(960, 803);



  /// ОБЩЕНИЕ С ПОЛЬЗОВВАТЕЛЕМ \\\

  // посылка
  try {
    s.write(str((x4+x3)/2+(y4+y3)/2*512));
    c = s.available();
  }
  catch (Exception e) {
  }
  // приёмка
  try {
    if (c != null) {
      input = c.readString();
      println(input);
    }
  }
  catch (Exception e) {
  }
}



/// ДОПОЛНИТЕЛЬНЫЕ ФУНКЦИИ \\\

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

// мусоросборщик
void GC() {
  System.gc(); 
  delay(100);
}

// установка цвета
void setcolor(int r, int g, int b) {
  stroke(r, g, b);      
  fill(r, g, b);
}
// квадратное сравнение
boolean ultraCompare(PImage pi, float where, int withR, int withG, int withB, int error) {
  try {
    if (compare(pi, where, withR, withG, withB, error)&&
      compare(pi, where-step, withR, withG, withB, error)&&compare(pi, where+step, withR, withG, withB, error)&&
      compare(pi, where-step*Color.width, withR, withG, withB, error)&&compare(pi, where+step*Color.width, withR, withG, withB, error)&&
      compare(pi, where-step+step*Color.width, withR, withG, withB, error)&&compare(pi, where-step-step*Color.width, withR, withG, withB, error)&&
      compare(pi, where+step+step*Color.width, withR, withG, withB, error)&&compare(pi, where+step-step*Color.width, withR, withG, withB, error))
      return true; 
    else 
    return false;
  } 
  catch (Exception e) {
    return false;
  }
}
// сравнение цвета
boolean compare(PImage pi, float where, int withR, int withG, int withB, int error) {
  try {
    if ((abs(red(pi.pixels[(int)where])-withR)<error)&&(abs(green(pi.pixels[(int)where])-withG)<error)&&(abs(blue(pi.pixels[(int)where])-withB)<error)) 
      return true; 
    else 
    return false;
  } 
  catch (Exception e) {
    return false;
  }
}

boolean isGrey (PImage pi, float where, int error) {
  try {
    float r = red(pi.pixels[(int)where]);
    float g = green(pi.pixels[(int)where]);
    float b = red(pi.pixels[(int)where]);
    float a = (r+g+b)/3;
    if ((abs(r-a)<error)&&(abs(g-a)<error)&&(abs(b-a)<error)) 
      return true; 
    else 
    return false;
  } 
  catch (Exception e) {
    return false;
  }
}

void mouseClicked() { 
  loadPixels(); 
  // Since we are going to access the image's pixels too  
  Color.loadPixels(); 
  int loc = mouseX + mouseY*width;

  float r = red(Color.pixels[loc]);
  float g = green(Color.pixels[loc]);
  float b = blue(Color.pixels[loc]);

  println(mouseX, " ", mouseY);          
  println(r, " ", g, " ", b);          

  updatePixels();
}
