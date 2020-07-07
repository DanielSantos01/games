package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Ground {
    protected Image groundImage;
    private int x = 0;
    private final Settings settings;
    
    public Ground(Settings set) throws IOException{
        settings = set;
        groundImage = ImageIO.read(getClass().getResource("..//assets//base.png"));
        groundImage = groundImage.getScaledInstance(2*(settings.screenWidth-16), groundImage.getHeight(settings.canvas), 0);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void display(Graphics g){
        if((settings.preStart || settings.start) && !(settings.touchPipe)) updatePostion();
        draw(g);
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void updatePostion(){
        x -= 5;
        checkOut();
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    private void draw(Graphics g){
        g.drawImage(groundImage, x, 680 - groundImage.getHeight(settings.canvas), settings.canvas);
    }
   
    //--------------------------------------------------------------------------------------------------------------------
    private void checkOut(){
        if(x <= -366) x = 0;
    }
}
