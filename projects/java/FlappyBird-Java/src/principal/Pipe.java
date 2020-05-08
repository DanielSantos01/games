
package principal;
import java.awt.Graphics;
import java.awt.Image;
import java.awt.geom.AffineTransform;
import java.awt.image.AffineTransformOp;
import java.awt.image.BufferedImage;
import java.io.IOException;
import javax.imageio.ImageIO;


public class Pipe {

    private Image pipeUpImage;
    private Image pipeDownImage;
    private final Settings settings;
    protected final int pipeUpHight[] = {250, 100, 300, 50, 200, 400, 350, 150, 30, 10};
    protected final int pipeDownHeight[] = {240, 390, 190, 440, 290, 90, 140, 340, 460, 480};
    protected int[] distances = {0, 0, 0, 0, 0, 0, 0, 0, 0, 0};
    protected int[] copy;
    int currentPipe = 0;
    
    public Pipe(Settings config) throws IOException{
        settings = config;
        configureImages();
    }
    
    public void draw(Graphics paintArea){
        if(settings.start || settings.gameOver){
            update(paintArea);
        }else if(settings.preStart && settings.configurePipes){
            configurePipes();
            settings.configurePipes = false;
        }
    }
    
    private void configurePipes(){
        for(int i = 0; i <= 9; i++){
            distances[i] = 450 + 4*i*50;
        }
    }
    
    private void update(Graphics paintArea){
        for(int i = 0; i <= 9; i++){
            updateDownPipes(paintArea, i);
            updateUpPipes(paintArea, i);
            if(!settings.gameOver)distances[i] -= 5;
        }
        checkPipeOut();
    }
    
    private void checkPipeOut(){
        if(distances[currentPipe] == -50){
            distances[currentPipe] = 1950;
            currentPipe++;
            if(currentPipe == 10){
                currentPipe = 0;
            }
        }
    }
    
    private void updateUpPipes(Graphics paintArea, int i){
        paintArea.drawImage(pipeUpImage, distances[i], 680-110 - pipeUpHight[i], 
                pipeDownImage.getWidth(settings.canvas), pipeUpHight[i], settings.canvas);
    }
    
    private void updateDownPipes(Graphics paintArea, int i){
        paintArea.drawImage(pipeDownImage, distances[i], 0,pipeUpImage.getWidth(settings.canvas),
                    pipeDownHeight[i], settings.canvas);
    }
    
    private void configureImages() throws IOException{
        pipeUpImage = ImageIO.read(getClass().getResource("..//assets//pipe-green.png"));
        AffineTransform tx = AffineTransform.getScaleInstance(1, -1);
        tx.translate(0, -pipeUpImage.getHeight(null));
        AffineTransformOp op = new AffineTransformOp(tx, AffineTransformOp.TYPE_NEAREST_NEIGHBOR);
        pipeDownImage = op.filter((BufferedImage)pipeUpImage, null);
    }
}
