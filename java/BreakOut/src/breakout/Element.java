package breakout;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Element {
    private final int width;
    private final int height;
    protected Rectangle rect;
    private final Image image;
    private Settings settings;
    
    public Element(Settings set) throws IOException{
        rect = new Rectangle();
        width = 100;
        height = 30;
        rect.width = width;
        rect.height = height;
        settings = set;
        image = ImageIO.read(getClass().getResource("..//images//element.png"));
    }
    
    public void draw(Graphics2D g){
        g.drawImage(image, rect.x, rect.y, rect.width, rect.height, settings.canvas);
    }
}
