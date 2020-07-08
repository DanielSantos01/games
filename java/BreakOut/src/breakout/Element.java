package breakout;

import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Element {
    private final Image image;
    private final Settings settings;
    protected Rectangle rect;
    
    public Element(Settings set) throws IOException{
        rect = new Rectangle(0, 0, 100, 30);
        settings = set;
        image = ImageIO.read(getClass().getResource("..//images//element.png"));
    }
    
    public void draw(Graphics2D g){
        g.drawImage(image, rect.x, rect.y, rect.width, rect.height, settings.canvas);
    }
}
