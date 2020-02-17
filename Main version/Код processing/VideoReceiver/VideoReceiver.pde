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
String input;
//String ad = "25.21.130.87";
//String ad = "192.168.1.34";
//String ad = "127.0.0.1";
//String ad = "10.0.0.19";
String ad = "25.12.173.173"; //клиент

void setup() {
  size(618, 424);
  try {
    ds = new DatagramSocket(port);
  } 
  catch (SocketException e) {
    e.printStackTrace();
  } 
  video = createImage(512, 424, RGB);

  c = new Client(this, ad, 12345);
  println(c.ip());
  image(loadImage("1.jpg"), 512, 0, 106, 106);
  image(loadImage("2.jpg"), 512, 106, 106, 106);
  image(loadImage("3.jpg"), 512, 212, 106, 106);
  image(loadImage("4.jpg"), 512, 318, 106, 106);
}

void draw() {
  checkForImage();
  image(video, 0, 0, 512, 424);

  if ((mousePressed)&&(mouseX>512)) { c.write( str(mouseY/106));  println(str(mouseY/106));}
  if (c.available() > 0) { input = c.readString(); println(input); }
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