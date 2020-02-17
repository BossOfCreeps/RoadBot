// Based on code by GeneKao (https://github.com/GeneKao)

ChildApplet child; 

void settings() {
  size(320, 240);
}

void setup() {
  surface.setTitle("Main sketch");
  child = new ChildApplet();
}

void draw() {
}

void mousePressed() {
}

void mouseDragged() {
}


class ChildApplet extends PApplet {
  //JFrame frame;

  public ChildApplet() {
    super();
    PApplet.runSketch(new String[]{this.getClass().getName()}, this);
  }

  public void settings() {
    size(400, 400);
  }
  
  public void setup() { 
  }

  public void draw() {

  }

  public void mousePressed() {
  }

  public void mouseDragged() {
  }
}