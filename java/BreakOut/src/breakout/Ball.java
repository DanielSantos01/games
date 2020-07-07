package breakout;

import java.awt.Graphics2D;
import java.awt.Rectangle;

public class Ball {
    Settings settings;
    
    //position
    protected final int startx;
    protected final int starty;
    protected final int radius;
    protected int moveValue;
    protected int x;
    protected int y;
    
    //movement flags
    private boolean up;
    private boolean down;
    
    private final Rectangle rect;
    private final Bar bar;
    
    public Ball(Settings set, Bar ba){
        settings = set;
        bar = ba;
        
        //position
        startx = 480;
        starty = 496;
        x = startx;
        y = starty;
        radius = 25;
        moveValue = 6;
        
        //movement flags
        up = false;
        down = false;
        
        rect = new Rectangle(x, y, 2*radius, 2*radius);
    }
    
    public void draw(Graphics2D g){
        rect.x = x;
        rect.y = y;
        g.fillArc(x, y, 2*radius, 2*radius, 0, 360);
    }
    
    public void checkEdges(){
        if(settings.start){
            if(y > 0 && !(down)){
                up = true;
                down = false;
            
            }else{
                up = false;
                down = true;
                if ((y+2*radius) >= settings.screenHeight) fail();
                  
            }
        }
    }
    
    public void checkMove(){
        
        if(up) y -= moveValue;
        
        if(down) y += moveValue;
        
    }
    
    public void checkCollisions(){
        
       if(rect.intersects(bar.rect) && settings.start) down = false;
       
    }
    
    public void fail(){
        up = false;
        down = false;
        x = startx;
        y = starty;
        bar.x = bar.startx;
        settings.preStart = true;
        settings.start = false;
    }
}
