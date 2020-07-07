package breakout;
import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;

public class Bar {
    Settings settings;
    
    //position
    protected final int width;
    protected final int height;
    protected final int startx;
    protected final int starty;
    protected int x;
    protected int moveValue;
    
    //rectangle
    protected Rectangle rect;
    
    public Bar(Settings set){
        settings = set;
        width = 200;
        height = 30;
        startx = 400;
        starty = 546;
        x = startx;
        moveValue = 5;
        rect = new Rectangle(x, starty, width, height);
    }
    
    public void draw(Graphics2D g){
        rect.x = x;
        g.setColor(Color.white);
        g.fillRect(x, starty, width, height);
    }
}
