package breakout;
import java.awt.Color;
import java.awt.Graphics2D;

public class Bar {
    Settings settings;
    protected final int width;
    protected final int height;
    protected final int startx;
    protected final int starty;
    protected int x;
    
    public Bar(Settings set){
        settings = set;
        width = 200;
        height = 30;
        startx = 400;
        starty = 546;
        x = startx;
    }
    
    public void draw(Graphics2D g){
        g.setColor(Color.white);
        g.fillRect(x, starty, width, height);
    }
}
