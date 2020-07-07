package principal;

import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Background {
    private final Image backgroundImage;
    private final Settings settings;
    private final int width;
    private final int height;
    
    public Background(Settings set) throws IOException{
        settings = set;
        backgroundImage = ImageIO.read(getClass().getResource("..//assets//background-day.png"));
        width = 400;
        height = 680;
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void drawBackground(Graphics g){
        g.drawImage(backgroundImage, 0, 0, width, height, settings.canvas);
    }
}
