package alieninvasion;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;

public class Bullet {
    protected Rectangle rect;
    private Ship ship;
    private Settings settings;
    protected boolean onScreen;
    
    public Bullet(Ship shp, Settings stt){
        ship = shp;
        rect = new Rectangle(ship.rect.x + (ship.rect.width/2), ship.rect.y-20, 3, 20);
        settings = stt;
        onScreen = true;
    }
    
    protected void shoot(Graphics2D g){
        if(onScreen){
            draw(g);
            update();
            checkPosition();
        }
    }
    
    private void draw(Graphics2D g){
        g.setColor(Color.gray);
        g.fillRect(rect.x, rect.y, rect.width, rect.height);
    }
    
    private void update(){
        rect.y -= 20;
    }
    
    private void checkPosition(){
        if((rect.y + rect.height) <= 0) onScreen = false;
    }
}
