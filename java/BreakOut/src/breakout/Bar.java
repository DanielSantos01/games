package breakout;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;

public class Bar {
    Settings settings;
    
    //position
    protected final int startx;
    protected final int starty;
    protected int moveValue;
    
    //rectangle
    protected Rectangle rect;
    
    public Bar(Settings set){
        startx = 400;
        starty = 546;
        moveValue = 20;
        settings = set;
        rect = new Rectangle(startx, starty, 200, 30);
    }
    
    protected void draw(Graphics2D g){
        g.setColor(Color.white);
        g.fillRect(rect.x, rect.y, rect.width, rect.height);
    }
    
    protected void reset(){
        rect.x = startx;
        if(settings.gameOver) moveValue = 20;
    }
    
}
