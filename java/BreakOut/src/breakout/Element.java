package breakout;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;

public class Element {
    private final int width;
    private final int height;
    protected Rectangle rect;
    
    public Element(){
        rect = new Rectangle();
        width = 100;
        height = 30;
        rect.width = width;
        rect.height = height;
    }
    
    public void draw(Graphics2D g){
        g.setColor(Color.white);
        g.fillRect(rect.x, rect.y, rect.width, rect.height);
    }
}
