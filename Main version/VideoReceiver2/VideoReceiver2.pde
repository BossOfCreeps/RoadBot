import javax.imageio.*;
import java.awt.image.*; 
import java.io.*;
import java.net.*;
import processing.net.*;

int port = 9010; 
DatagramSocket ds; 
byte[] buffer = new byte[65536]; 
PImage video;

Client c;
int input;
//String ad = "25.21.130.87";
//String ad = "192.168.1.34";
//String ad = "127.0.0.1";
//String ad = "10.0.0.19";
String ad = "25.12.173.173"; //клиент

void setup() {
  size(800, 600);
  try {
    ds = new DatagramSocket(port);
  } 
  catch (SocketException e) {
    e.printStackTrace();
  } 
  video = createImage(800, 600, RGB);

  c = new Client(this, ad, 12345);
  println(c.ip());
}

void draw() {
  checkForImage();
  image(video, 0, 0);
  //if ((mousePressed)&&(mouseX>512)) { c.write( str(mouseY/106));  println(str(mouseY/106));}
  //if (c.available() > 0) { input = c.readString(); println(input); }
  
   if ((mousePressed == true)&&(mouseX>512)) { 
    c.write( str(mouseY/106));  
    println(str(mouseY/106));
  }
 if (c.available() > 0) { 
    input = int(c.readString()); 
    ellipse(input%512, input/512, 10, 10);
    //    String[] list = split(input, " ");

    //println(list[0],"!",list[1]);
  }
}

void checkForImage() {
  DatagramPacket p = new DatagramPacket(buffer, buffer.length); 
  try {
    ds.receive(p);
  } 
  catch (IOException e) {
    e.printStackTrace();
  } 
  byte[] data = p.getData();

  ByteArrayInputStream bais = new ByteArrayInputStream( data );

  video.loadPixels();
  try {
    BufferedImage img = ImageIO.read(bais);
    img.getRGB(0, 0, video.width, video.height, video.pixels, 0, video.width);
  } 
  catch (Exception e) {
    e.printStackTrace();
  }
  video.updatePixels();
}
