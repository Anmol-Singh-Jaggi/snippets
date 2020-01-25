import java.awt.AWTException;
import java.awt.Robot;
import java.awt.event.InputEvent;
import java.awt.MouseInfo;
 

public class Mulate {
  private static final int delaySeconds = 30;
  public static void click(int x, int y) {
    try {
      Robot bot = new Robot();
      bot.mouseMove(x, y);
      //bot.mousePress(InputEvent.BUTTON1_MASK);
      //bot.mouseRelease(InputEvent.BUTTON1_MASK);
      bot.delay(delaySeconds * 1000);
    }
    catch (Exception e) {
      // TODO Auto-generated catch block
      e.printStackTrace();
    }
  }

  
  public static void moveToPredefined(String[] args){
    int[] posListX = {300, 500};
    int[] posListY = {300, 500};
    if(args.length >= 4)
    {
      posListX[0] = Integer.parseInt(args[0]);
      posListY[0] = Integer.parseInt(args[1]);
      posListX[1] = Integer.parseInt(args[2]);
      posListY[1] = Integer.parseInt(args[3]);
    }

    while (true) {
      for (int i = 0; i < posListX.length; i++) {
        int x = posListX[i];
        int y = posListY[i];
        click(x, y);
      }
    }
  }

  
  public static void moveToDiff(){
    int[] diffX = {5, -5};
    int[] diffY = {5, -5};
    while (true) {
      for (int i = 0; i < diffX.length; i++) {
        int mousePosX = MouseInfo.getPointerInfo().getLocation().x;
        int mousePosY = MouseInfo.getPointerInfo().getLocation().y;
        mousePosX += diffX[i];
        mousePosY += diffY[i];
        click(mousePosX, mousePosY);
      }
    }
  }
 
  public static void main(String[] args) {
    System.out.println("Running...");
    moveToDiff();
  }

}