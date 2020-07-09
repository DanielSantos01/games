package breakout;

import java.awt.Graphics2D;

public class Status {
    protected int level;
    protected int value;
    protected int chancesLeft;
    private String chancesMessage;
    private String scoreMessage;
    
    public Status(){
        level = 1;
        value = 0;
        chancesLeft = 3;
        chancesMessage = "Chances: " + chancesLeft;
        scoreMessage = "Level: " + level + " - Score: " + value;
    }
    
    protected void draw(Graphics2D g){
        chancesMessage = "Chances: " + chancesLeft;
        g.drawString(chancesMessage, 0, 20);
        scoreMessage = "Level: " + level + " - Score: " + value;
        g.drawString(scoreMessage, 800, 20);
    }
}
