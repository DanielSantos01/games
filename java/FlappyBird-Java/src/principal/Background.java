package principal;
import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;

public class Background {
    private final Image backgroundImage;
    private final Settings settings;
    
    public Background(Settings config) throws IOException{
        settings = config;
        backgroundImage = ImageIO.read(getClass().getResource("..//assets//background-day.png"));
    }
    
    //--------------------------------------------------------------------------------------------------------------------
    public void drawBackground(Graphics g){
        g.drawImage(backgroundImage, 0, 0, 400, 680, settings.canvas);
    }
}
