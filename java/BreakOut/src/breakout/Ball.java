package breakout;

import java.awt.Graphics2D;
import java.awt.Rectangle;

public final class Ball {
    Settings settings;
    
    //position
    private final int startx;
    private final int starty;
    private final int radius;
    private int verticalValue;
    private int horizontalValue;
    private int center;
    
    //movement flags
    private boolean up;
    private boolean down;
    private boolean left;
    private boolean right;
    private boolean allow;
    
    protected final Rectangle rect;
    private final Bar bar;
    private final Score score;
    
    public Ball(Settings set, Bar ba, Score scor){
        settings = set;
        bar = ba;
        score = scor;
        
        //position
        startx = 480;
        starty = 506;
        radius = 20;
        verticalValue = 8;
        
        //movement flags
        resetFlags();
        
        //ball rect
        rect = new Rectangle(startx, starty, 2*radius, 2*radius);
    }
    
    protected void execute(Graphics2D g){
        draw(g);
        if(settings.start){
            checkEdges();
            move();
        }
    }
    
    private void draw(Graphics2D g){
        center = rect.x + (rect.width/2);
        g.fillArc(rect.x, rect.y, 2*radius, 2*radius, 0, 360);
    }
    
    private void checkEdges(){
        //movimento vertical
        if(rect.y > 0 && !(down)){
            goUp();
        }else{
            goDown();
            if ((rect.y + 2*radius) >= settings.screenHeight) reset("fail");    
        }
        
        //movimento horizontal
        if(rect.x > 0 && !(right) && allow){
            goLeft();
        }else if(allow){
            goRight();
            if((rect.x + 2*radius) >= settings.screenWidth) goLeft();
        }
    }
    
    private void move(){
        if(up) rect.y -= verticalValue;
        
        else if(down) rect.y += verticalValue;
        
        if(right) rect.x += horizontalValue;
        
        else if(left) rect.x -= horizontalValue;
    }
    
    protected void reset(String cause){
        rect.x = startx;
        rect.y = starty;
        resetFlags();
        bar.reset();
        
        switch(cause){
            case "fail":
                score.chancesLeft--;
                if(score.chancesLeft == 0) {
                    settings.preStart = false;
                    settings.gameOver = true;
                    verticalValue = 8;
                }
                break;
                
            case "new level":
                verticalValue += 1;
                break;
            
            default:
                break;
        }
        
    }
    
    protected void resetFlags(){
        up = false;
        down = false;
        right = false;
        left = false;
        allow = false;
        settings.preStart = true;
        settings.start = false;
    }
    
    protected void changeDirection(){
        if(down) goUp();
        else if(up) goDown();
    }
    
    protected void touchBar(int centerBar){
      if(center > centerBar){
          if(center < (centerBar+40)) horizontalValue = 1;
          else if(center < (centerBar+75)) horizontalValue = 2;
          else if(center < (centerBar+100)) horizontalValue = 3;
          allow = true;
          goRight();
      }else if (center < centerBar){
          if(center > (centerBar-40)) horizontalValue = 1;
          else if(center > (centerBar-75)) horizontalValue = 2;
          else if(center > (centerBar-100)) horizontalValue = 3;
          allow = true;
          goLeft();
      }
      goUp();
    }
    
    private void goUp(){
        up = true;
        down = false;
    }
    
    private void goDown(){
        up = false;
        down = true;
    }
    
    private void goLeft(){
        left = true;
        right = false;
    }
    
    private void goRight(){
        left = false;
        right = true;
    }
}
