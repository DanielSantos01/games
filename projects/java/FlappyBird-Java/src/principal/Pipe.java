
package principal;
import java.awt.Canvas;
import java.awt.Graphics;
import java.awt.Image;
import java.io.IOException;
import javax.imageio.ImageIO;


public class Pipe {
    Graphics paintArea;
    Background back;
    protected Image pipeImage;
    
    public Pipe(Graphics g, Background bg) throws IOException{
        paintArea = g;
        back = bg;
        pipeImage = ImageIO.read(getClass().getResource("..//assets//pipe-green.png"));
    }
    
    public void paintPipe(Canvas canvas){
        paintArea.drawImage(pipeImage, 0, 0, canvas);
    }
    
}
