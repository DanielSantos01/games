package breakout;

import java.awt.Graphics2D;

public class Score {
    protected int level;
    protected int value;
    protected int left;
    private String chancesMessage;
    private String scoreMessage;
    
    public Score(){
        level = 1;
        value = 0;
        left = 3;
        chancesMessage = "Chances: " + left;
        scoreMessage = "Level: " + level + " - Score: " + value;
    }
    
    protected void draw(Graphics2D g){
        chancesMessage = "Chances: " + left;
        g.drawString(chancesMessage, 0, 20);
        scoreMessage = "Level: " + level + " - Score: " + value;
        g.drawString(scoreMessage, 800, 20);
    }
}
