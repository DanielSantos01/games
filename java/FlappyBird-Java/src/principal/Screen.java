package principal;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;
import javax.swing.JFrame;

public final class Screen extends JFrame{
    private final Image iconImage;
    
    public Screen(Settings settings, KeyEvents key) throws IOException{
        iconImage = ImageIO.read(getClass().getResource("..//assets//bluebird-midflap.png"));
        add(settings.canvas);
        addKeyListener(key);
        setSize(settings.screenWidth, settings.screenHeight);
        setIconImage(iconImage);
        setTitle("Flappy Bird - Java");
        setVisible(true);
        setResizable(false);
        setLocationRelativeTo(null);
        setDefaultCloseOperation(JFrame.EXIT_ON_CLOSE);
    }
}
