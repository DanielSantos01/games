package breakout;

import java.awt.Graphics2D;

public class Ball {
    Settings settings;
    
    //position
    protected final int initialx;
    protected final int initialy;
    protected final int radius;
    protected int centerx;
    protected int x;
    protected int y;
    protected int moveValue;
    
    //movement flags
    private boolean up;
    private boolean down;
    
    public Ball(Settings set){
        settings = set;
        
        //position
        initialx = 480;
        initialy = 496;
        x = initialx;
        y = initialy;
        radius = 25;
        centerx = x + radius;
        moveValue = 6;
        
        //movement flags
        up = false;
        down = false;
    }
    
    public void draw(Graphics2D g){
        g.fillArc(x, y, 2*radius, 2*radius, 0, 360);
        centerx = x + radius;
    }
    
    public void checkEdges(){
        if(settings.start){
            if(y > 0 && !(down)){
                up = true;
                down = false;
            
            }else{
                up = false;
                down = true;
                if ((y+2*radius) >= settings.screenHeight) down = false;   
            }
        }
        
    }
    
    public void checkMove(){
        
        if(up) y -= moveValue;
        
        if(down) y += moveValue;
        
    }
}
