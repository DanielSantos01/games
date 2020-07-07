package principal;
import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Ground {
    protected Image ground;
    private int x_position = 0;
    private final Settings settings;
    
    public Ground(Background bg, Settings config) throws IOException{
        settings = config;
        ground = ImageIO.read(getClass().getResource("..//assets//base.png"));
        ground = ground.getScaledInstance(2*(settings.canvas.getWidth() - 16), ground.getHeight(config.canvas), 0);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void move(Graphics g){
        if((settings.preStart || settings.start) && !(settings.touchPipe)){
            drawGround(g);
            updatePostion();
        }
        drawGround(g);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void updatePostion(){
        x_position -= 5;
        checkOut();
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void drawGround(Graphics g){
        g.drawImage(ground, x_position, 680 - ground.getHeight(settings.canvas), settings.canvas);
    }
   
    //--------------------------------------------------------------------------------------------------------------------
    private void checkOut(){
        if(x_position <= -384) x_position = 0;
    }
}
