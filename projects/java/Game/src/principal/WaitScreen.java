package principal;
import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class WaitScreen {
    private final Image preStart;
    private final Image gameOver;
    private final Settings settings;
    
    public WaitScreen(Settings config) throws IOException{
        settings = config;
        preStart = ImageIO.read(getClass().getResource("..//assets//message.png"));
        gameOver = ImageIO.read(getClass().getResource("..//assets//gameover.png"));
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void drawWaitScreen(Graphics g){
        if(settings.preStart){
            drawPreStartButton(g);
        }else{
            drawGameOverButton(g);
        }
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void drawPreStartButton(Graphics g){
        g.drawImage(preStart, 115, 108, settings.canvas);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void drawGameOverButton(Graphics g){
        g.drawImage(gameOver, 115, 108, settings.canvas);
    }
}
