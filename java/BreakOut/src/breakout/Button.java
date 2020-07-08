
package breakout;

import java.awt.Color;
import java.awt.Graphics2D;
import java.awt.Rectangle;


public class Button {
    private final Rectangle rect;
    private final Settings settings;
    private String message;
    
    public Button(Settings set){
        rect = new Rectangle(400, 200, 200, 40);
        settings = set;
    }
    
    protected void draw(Graphics2D g){
        if(settings.preStart) startButton(g);
        else gameOverButton(g);
    }
    
    private void startButton(Graphics2D g){
        message = "press space to start";
        g.setColor(Color.blue);
        g.fillRect(rect.x, rect.y, rect.width, rect.height);
        g.setColor(Color.white);
        g.drawString(message, rect.x+37, rect.y+23);
    }
    
    private void gameOverButton(Graphics2D g){
        message = "Game Over";
        g.setColor(Color.blue);
        g.fillRect(rect.x, rect.y, rect.width, rect.height);
        g.setColor(Color.white);
        g.drawString(message, rect.x+65, rect.y+23);
    }  
}
