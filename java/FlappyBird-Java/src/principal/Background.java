package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Background {
    private final Image image;
    private final Settings settings;
    
    public Background(Settings set) throws IOException{
        settings = set;
        image = ImageIO.read(getClass().getResource("..//assets//background-day.png"));
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void drawBackground(Graphics g){
        g.drawImage(image, 0, 0, settings.screenWidth, settings.screenHeight, settings.canvas);
    }
}
