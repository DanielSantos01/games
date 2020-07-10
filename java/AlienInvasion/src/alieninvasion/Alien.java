package alieninvasion;

import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.Rectangle;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Alien {
    private final Image image;
    private final Settings settings;
    private boolean left, right;
    protected boolean touch;
    protected Rectangle rect;
    
    
    public Alien(Settings set) throws IOException{
        settings = set;
        left = false;
        right = true;
        touch = false;
        image = ImageIO.read(getClass().getResource("../images/alien.bmp"));
        rect = new Rectangle(0, 0, image.getWidth(settings.canvas), image.getHeight(settings.canvas));
    }
    
    protected void execute(Graphics2D g){
        draw(g);
        updatePosition();
        checkEdges();
    }
    
    private void draw(Graphics2D g){
        g.drawImage(image, rect.x, rect.y, rect.width, rect.height, settings.canvas);
    }
    
    private void updatePosition(){
        if(right) rect.x += 5;
        else rect.x -= 5;
    }
    
    private void checkEdges(){
        if(((rect.x + rect.width) >= settings.screenWidth) || (rect.x <= 0)) touch = true;
    }
    
    private void goRight(){
        right = true;
        left = false;
    }
    
    private void goLeft(){
        right = false;
        left = true;
    }
    
    protected void changeDirection(){
        if(right) goLeft();
        else goRight();
    }
    
    protected void goDown(){
        rect.y += 10;
        touch = false;
    }
    
}
