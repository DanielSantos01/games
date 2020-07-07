package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class WaitScreen {
    private final Image preStart;
    private final Image gameOver;
    private final Settings settings;
    private final int x;
    private final int y;
    
    public WaitScreen(Settings set) throws IOException{
        settings = set;
        x = 115;
        y = 108;
        preStart = ImageIO.read(getClass().getResource("..//assets//message.png"));
        gameOver = ImageIO.read(getClass().getResource("..//assets//gameover.png"));
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void draw(Graphics g){
        if(settings.preStart) drawPreStartButton(g);
        else drawGameOverButton(g);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void drawPreStartButton(Graphics g){
        g.drawImage(preStart, x, y, settings.canvas);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void drawGameOverButton(Graphics g){
        g.drawImage(gameOver, x, y, settings.canvas);
    }
}
