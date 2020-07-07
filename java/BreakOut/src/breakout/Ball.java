package breakout;

import java.awt.Graphics2D;

public class Ball {
    protected final int initialx;
    protected final int initialy;
    protected final int radius;
    protected int x;
    protected int y;
    Settings settings;
    
    public Ball(Settings set){
        initialx = 480;
        initialy = 496;
        radius = 50;
        x = initialx;
        y = initialy;
    }
    
    public void draw(Graphics2D g){
        g.fillArc(x, y, radius, radius, 0, 360);
    }
}
