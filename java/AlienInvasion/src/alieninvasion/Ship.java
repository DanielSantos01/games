package alieninvasion;

import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Ship {
    private final Image image;
    private final Settings settings;
    protected Rectangle rect;
    private final int initialx, initialy;
    
    public Ship(Settings set) throws IOException{
        settings = set;
        image = ImageIO.read(getClass().getResource("../images/ship.bmp"));
        initialx = (settings.screenWidth/2) - (image.getWidth(settings.canvas)/2);
        initialy = settings.screenHeight - (image.getHeight(settings.canvas)+25);
        rect = new Rectangle(initialx, initialy, image.getWidth(settings.canvas), image.getHeight(settings.canvas));
    }
    
    protected void run(Graphics2D g){
        draw(g);
    }
    
    private void draw(Graphics2D g){
        g.drawImage(image, rect.x, rect.y, rect.width, rect.height, settings.canvas);
    }
    
    protected void center(){
        rect.x = initialx;
    }
}
